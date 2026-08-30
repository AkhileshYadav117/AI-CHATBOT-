# 🤖 AI CHATBOT

### AI-Powered Conversation Assistant using Python & Groq API

> A high-performance Python conversational assistant that captures, cleans, and processes conversation data using Large Language Models via Groq's low-latency inference engine.

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Groq-API-F55036?style=for-the-badge)](https://groq.com/)
[![GitHub](https://img.shields.io/badge/Repository-AkhileshYadav117-181717?style=for-the-badge&logo=github)](https://github.com/AkhileshYadav117/AI-CHATBOT-)
[![License](https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge)](#-license)

---

## 📖 Overview

**AI CHATBOT** is an end-to-end Python implementation demonstrating modern LLM integration and data pipeline workflows. It captures screen/cursor-level conversation context, sanitizes input strings, constructs optimized prompts, and streams requests to the **Groq Cloud API** for ultra-fast response generation.

---

## ✨ Key Features

* **⚡ Ultra-Low Latency:** Leverages Groq LPUs for rapid inference.
* **🧹 Automated Data Sanitization:** Cleans and normalizes incoming conversation streams.
* **🧠 Context-Aware Prompting:** Dynamically structures inputs for high-accuracy completions.
* **🔐 Production-Safe Config:** Secures sensitive API credentials using `.env` handling.
* **📦 Modular Architecture:** Divided into distinct capture, API, and bot execution scripts.

---

## 🏗️ System Architecture

```text
┌─────────────────────────┐
│ Conversation Input Data │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Text Preprocessing      │ (01_get_cursor.py)
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Data Sanitization Engine│
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Dynamic Prompt Builder  │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Groq Cloud API Gateway  │ (02_groq.py)
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ LLM Inference Engine    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Execution & AI Response │ (03_bot.py)
└─────────────────────────┘
```

---

## 🛠️ Tech Stack

* **Core Language:** Python 3.11+
* **LLM Provider:** Groq Cloud API
* **Environment Management:** `python-dotenv`
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
AI-CHATBOT/
│
├── 01_get_cursor.py     # Captures and extracts cursor/screen context
├── 02_groq.py           # Handles Groq API authentication and payloads
├── 03_bot.py            # Primary chatbot runner and orchestration script
├── .env.example         # Template for environment variables
├── .gitignore           # Ignores sensitive credentials and local artifacts
├── requirements.txt     # Locked project dependencies
└── README.md            # Technical documentation
```

---

## 🚀 Quickstart Guide

### Prerequisites

* Python 3.11 or higher
* Groq API Key ([Get an API Key](https://console.groq.com/keys))

### 1. Clone & Set Up Directory

```bash
git clone [https://github.com/AkhileshYadav117/AI-CHATBOT-.git](https://github.com/AkhileshYadav117/AI-CHATBOT-.git)
cd AI-CHATBOT-
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Duplicate the template and add your credentials:

```bash
cp .env.example .env
```

Open `.env` and set your key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the Application

```bash
python 03_bot.py
```

---

## 🔐 Security Best Practices

* API credentials are kept strictly isolated from code using environment variables.
* The `.env` file is excluded from source control via `.gitignore`.
* A sanitized `.env.example` is maintained for safe collaboration.


## 👨‍💻 Author

**Akhilesh Yadav**  
*Computer Science & Engineering (Artificial Intelligence & Machine Learning)*  
GitHub: [@AkhileshYadav117](https://github.com/AkhileshYadav117)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Support

If you found this project useful or interesting, please consider giving it a ⭐ Star on GitHub.

<div align="center">

🤖 **Built with Python + Groq + AI**  
Made with ❤️ by **Akhilesh Yadav**

</div>