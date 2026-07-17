import os
from openai import OpenAI

# Old SDK (Legacy)
import google.generativeai as legacy_genai

# New SDK (Recommended)
from google import genai as new_genai
from anthropic import Anthropic

SUPPORTED_PROVIDERS = {"openai", "gemini", "anthropic"}


class LLMProvider:
    def __init__(self, config: dict):
        self.provider = config["provider"]

        if self.provider not in SUPPORTED_PROVIDERS:
            raise ValueError(
                f"Unsupported provider: {self.provider}. "
                f"Supported providers: {', '.join(SUPPORTED_PROVIDERS)}"
            )

        if self.provider not in config.get("models", {}):
            raise ValueError(f"No model configured for provider: {self.provider}")

        self.model = config["models"][self.provider]

        print(f"Provider    : {self.provider}")
        print(f"Model       : {config['models'][self.provider]}")
        print("=" * 50)

        if self.provider == "openai":
            key = os.getenv("OPENAI_API_KEY")
            if not key:
                raise ValueError("OPENAI_API_KEY env variable was not set ❌.")
            self.client = OpenAI(api_key=key)
        elif self.provider == "gemini":
            key = os.getenv("GEMINI_API_KEY")
            if not key:
                raise ValueError("GEMINI_API_KEY env variable was not set ❌.")

            # Old SDK (Legacy)
            # legacy_genai.configure(api_key=key)
            # self.client = legacy_genai.GenerativeModel(self.model)

            # New SDK (Recommended)
            self.client = new_genai.Client(api_key=key)
        elif self.provider == "anthropic":
            key = os.getenv("ANTHROPIC_API_KEY")
            if not key:
                raise ValueError("ANTHROPIC_API_KEY env variable was not set ❌.")
            self.client = Anthropic(api_key=key)
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")
        print(f"{self.provider.title()} client initiated successfully. ✅")

    def chat(self, user_message: str) -> str:
        try:
            if self.provider == "openai":
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": user_message}],
                )
                return response.choices[0].message.content
            elif self.provider == "gemini":
                # Old SDK (Legacy)
                # response = self.client.generate_content(user_message)

                # New SDK (Recommended)
                response = self.client.models.generate_content(
                    model=self.model, contents=user_message
                )
                return response.text
            elif self.provider == "anthropic":
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=1024,
                    messages=[{"role": "user", "content": user_message}],
                )
                return response.content[0].text

        except Exception as e:
            raise Exception(f"Error in {self.provider} chat: {str(e)}")
