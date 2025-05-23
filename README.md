# 💬 Groq Chatbot Implementation

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)


A powerful, responsive chatbot framework — powered by Groq API — supporting conversational AI, context-aware responses, and multiple implementation architectures.

## ✨ Features

* ✅ One-click setup for conversational AI
* 💬 Context-aware responses with memory functionality
* 🔄 Multiple implementation architectures for different use cases
* 🎯 FastAPI integration for scalable deployment
* 🧠 Smart response generation using Groq's language model
* 📊 Live conversation history tracking
* 💡 Clear error handling and debugging support
* 🖥️ No command line required for basic usage

## 🏗️ Architecture Overview

```
Groq Chatbot Framework
│
├— FastAPI Implementation (apigroq.py)
├— Command Line Chatbot (groq.py)
├— Context-Aware Chatbot (bot.py)
├— Memory-Enabled Chatbot (memory.py)
├— Vector Store Index Chatbot (chatbot.py)
├— LangChain Integration (ext.py)
├— Confidence Chat Engine (condence.py)
├— Automatic Restart Utility (watch_and_run.py)
└— Requirements Management (requirements.txt)
```

## 🎮 Getting Started

### 📦 Requirements

* Python 3.7+
* Groq API key
* Dependencies (from `requirements.txt`)

### 🔧 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/groq-chatbot.git
cd groq-chatbot

# Install dependencies
pip install -r requirements.txt

# Add API key
echo MyApi = 'your_api_key' > API.py
```

### ▶️ Usage

To run different chatbot implementations:

```bash
# FastAPI server
python apigroq.py

# Command-line chatbot
python groq.py

# Context-aware chatbot
python bot.py
```

## 📚 User Guide

1. Set up your environment.
2. Choose an implementation based on your needs.
3. Run the respective script.
4. Interact naturally. Type 'exit' to quit.

## 🔪 Developer Notes

* API key management
* Context loading and memory
* LangChain + Groq API usage
* Logging & error handling

## 📜 License

MIT License — See `LICENSE` file for full details.

## 🙌 Acknowledgements

Thanks to **Groq**, **LangChain**, **FastAPI**, and the **open-source community**.

---

###
