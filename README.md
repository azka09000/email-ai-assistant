# 📧 AI Email Assistant

An AI-powered email assistant that helps you **analyze, summarize, classify, and generate replies** for emails using LLMs. Built with **Streamlit + OpenRouter API (LLaMA 3.1)**.

---

## 🚀 Features

### 🧠 Email Classification
- Detects email type:
  - Job Opportunity
  - Meeting Request
  - Task Assignment
  - Inquiry
  - Spam / Promotional
  - General
- Assigns priority level:
  - High / Medium / Low
- Provides short reasoning

### 📄 AI Email Summarization
- Converts long emails into concise bullet points
- 5–7 key points only
- Focus on actions, decisions, and important details

### ✍️ AI Reply Generator
- Generates professional email replies
- Supports tone control:
  - Professional
  - Friendly
  - Concise
- Ready-to-send structured responses

### 🎨 Clean UI (Streamlit)
- Two-column layout (Summary | Reply)
- Classification dashboard
- Card-based UI with improved readability
- Interactive buttons for each AI function

---

## 🛠️ Tech Stack

- Python 🐍
- Streamlit 🎈
- OpenAI SDK (OpenRouter API)
- LLaMA 3.1 (meta-llama/llama-3.1-8b-instruct)
- dotenv

---

## 📂 Project Structure
EMAIL-ASSISTANT/
│
├── .streamlit/
│   └── config.toml
│
├── .venv/
│
├── app/
│   └── streamlit_app.py
│
├── services/
│   └── llm_service.py
│
├── .env
├── .gitignore
├── list_models.py
├── README.md
└── requirements.txt
---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone 
cd email-assistant

### 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Add API key
Create a `.env` file:
OPENROUTER_API_KEY=your_api_key_here

### 5. Run the app
streamlit run app/streamlit_app.py

---

## 📸 UI Overview

- Paste email → Click action buttons
- Get:
  - 📄 Summary
  - 🧠 Classification
  - ✍️ Reply

---

## 💡 Example Use Cases

- Students managing internship emails
- Professionals handling high email volume
- HR teams screening applications
- Productivity automation workflows

---

## 🔮 Future Improvements

- One-click "Auto Mode" (full pipeline execution)
- Email history storage
- Export to PDF / DOCX
- Gmail API integration
- Smart reply suggestions based on context

---

## 📌 Author

Built by **Azka Nisar**  
AI Student | Aspiring ML Engineer | Builder of practical AI tools

---

## ⭐ If you like this project
Consider giving it a star ⭐ and connecting on LinkedIn!