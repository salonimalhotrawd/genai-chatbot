# 🤖 Multi-Provider CLI Chatbot

A simple Command Line Interface (CLI) chatbot built using Python that supports multiple Large Language Model (LLM) providers through a common interface.

Currently supported providers:

- ✅ OpenAI
- ✅ Google Gemini
- ✅ Anthropic Claude

The project is designed to demonstrate how different LLM APIs can be integrated with minimal code changes using a configurable provider architecture.

---

# 🚀 Features

- Multiple LLM provider support
- Configuration-based provider switching
- Environment variable API key management
- Common interface for all providers
- Input validation
- Error handling
- Beginner-friendly code structure
- Easy to extend for new providers

---

# 📁 Project Structure

```
chatbot/
│
├── main.py
├── llm_provider.py
├── config.json
├── .env
├── requirements.txt
├── README.md
└── myenv/
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <repository-url>
cd chatbot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv myenv
```

Activate

```bash
myenv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv myenv
source myenv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
ANTHROPIC_API_KEY=your_anthropic_key
```

---

# ⚙️ Configuration

Example `config.json`

```json
{
    "provider": "gemini",
    "models": {
        "openai": "gpt-4o-mini",
        "gemini": "gemini-2.5-flash",
        "anthropic": "claude-sonnet-4-20250514"
    }
}
```

To switch providers simply change:

```json
"provider": "openai"
```

or

```json
"provider": "gemini"
```

or

```json
"provider": "anthropic"
```

No code changes are required.

---

# ▶️ Run the Project

```bash
python main.py
```

Example

```
==================================================
Simple CLI Chatbot
==================================================

Provider : Gemini
Model    : gemini-2.5-flash

You:
```

---

# 🏗️ Architecture

```
                +----------------+
                |   main.py      |
                +--------+-------+
                         |
                         |
                +--------v-------+
                |  LLMProvider   |
                +--------+-------+
                         |
     ----------------------------------------
     |                  |                   |
     |                  |                   |
+----v----+      +------v------+     +------v------+
| OpenAI  |      |   Gemini    |     | Anthropic   |
+---------+      +-------------+     +-------------+
```

---

# Supported Providers

## OpenAI

Library

```python
from openai import OpenAI
```

API

```python
client.chat.completions.create(...)
```

---

## Google Gemini

### Legacy SDK

```python
import google.generativeai as genai
```

```python
genai.configure(...)
model.generate_content(...)
```

### New SDK (Recommended)

```python
from google import genai
```

```python
client.models.generate_content(...)
```

> **Note:** This project uses the new `google-genai` SDK. The legacy SDK is kept as commented reference for learning purposes.

---

## Anthropic Claude

```python
from anthropic import Anthropic
```

```python
client.messages.create(...)
```

---

# Error Handling

The application validates:

- Supported provider
- Config file
- Config values
- API keys
- Missing model configuration
- Runtime API exceptions

---

# How to Add a New Provider

1. Add the provider name to:

```python
SUPPORTED_PROVIDERS
```

2. Configure the client inside `LLMProvider.__init__()`.

3. Add the chat implementation inside `chat()`.

4. Add the model in `config.json`.

No changes are required in `main.py`.

---

# Technologies Used

- Python
- OpenAI SDK
- Google GenAI SDK
- Anthropic SDK
- python-dotenv

---

# Learning Objectives

This project demonstrates:

- Working with multiple LLM providers
- API key management
- Configuration-driven development
- Exception handling
- Object-Oriented Programming (OOP)
- Clean project structure
- Provider abstraction

---

# Future Improvements

- Conversation History (Memory)
- Streaming Responses
- System Prompts
- Temperature & Max Tokens from Config
- Local LLM Support (Ollama)
- Hugging Face Models
- Prompt Templates
- Logging
- Unit Tests
- Docker Support
- CLI Arguments
- Web UI (Streamlit / Gradio)
- Retrieval-Augmented Generation (RAG)

---

# Requirements

```
openai
google-genai
anthropic
python-dotenv
ollama
transformers
huggingface_hub
```

---

# Author

**Saloni Malhotra**

Learning Generative AI through hands-on projects by building practical applications with multiple LLM providers.
