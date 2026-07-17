import os
import json
from dotenv import load_dotenv
from llm_provider import LLMProvider

EXIT_COMMANDS = {"exit", "quit"}


def load_config(config_path: str = "config.json") -> dict:
    """
    Load chatbot configuration from JSON file.
    """
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {config_path} ❌")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid json in the config file: {config_path} ❌")


def run_chat():
    print("=" * 50)
    print(" Simple CLI Chatbot ")
    print("=" * 50)

    try:
        config = load_config()

        chatbot = LLMProvider(config)

    except Exception as e:
        print(f"Initilization Error: {e}")
        return

    while True:
        user_input = input("You: 🤵 ")

        if user_input.lower() in EXIT_COMMANDS:
            print("Goodbye 🙋‍♂️😊 ")
            break

        if not user_input.strip():
            print("Please enter a valid question or message for the bot: ")
            continue

        try:
            reply = chatbot.chat(user_message=user_input)
            print(f"Bot: {reply}\n")

        except Exception as e:
            print(f"Error with chat {str(e)}")


if __name__ == "__main__":
    load_dotenv()
    run_chat()
