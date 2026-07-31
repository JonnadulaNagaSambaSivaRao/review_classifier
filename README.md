# 🌟 Customer Review Sentiment Analysis using Groq LLM 🤖

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Prompt%20Engineering-AI-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Sentiment%20Analysis-NLP-purple?style=for-the-badge">
</p>

---

## 🚀 Project Overview

**Customer Review Sentiment Analysis** is an AI-powered application that analyzes customer feedback and classifies it into three sentiment categories:

🟢 **Positive**  
🟡 **Neutral**  
🔴 **Negative**

This project uses **Groq LLM with Llama 3.3 70B model** and **Prompt Engineering techniques** to understand the emotion and meaning behind customer reviews.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 AI Sentiment Detection | Uses Groq Large Language Model |
| 📝 Customer Review Input | Accepts user review dynamically |
| 🎯 Accurate Classification | Categorizes reviews into Positive, Neutral, Negative |
| 🔐 Secure API Handling | Uses `.env` file for API key protection |
| ⚡ Fast Response | Powered by Groq high-speed inference |
| 🧠 Prompt Engineering | Uses optimized instructions for better results |

---

# 🏗️ Project Workflow

```
        👤 Customer Review
                |
                ▼
        📝 Prompt Creation
                |
                ▼
        🤖 Groq LLM
        (Llama 3.3 70B)
                |
                ▼
     ┌──────────┬──────────┬──────────┐
     ▼          ▼          ▼
 🟢 Positive 🟡 Neutral 🔴 Negative
```

---

# 🛠️ Technologies Used

<div>

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Programming Language |
| 🤖 Groq API | LLM Model Access |
| 🦙 Llama 3.3 70B | Sentiment Classification Model |
| 🔑 python-dotenv | Environment Variable Management |
| 🧠 Prompt Engineering | AI Instruction Design |

</div>

---

# 📂 Project Structure

```
Customer-Sentiment-Analysis/
│
├── main.py              # Main Python Application
├── .env                 # API Key Configuration
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/customer-sentiment-analysis.git
```

## 2️⃣ Navigate into Project

```bash
cd customer-sentiment-analysis
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install groq python-dotenv
```

---

# 🔐 Environment Configuration

Create a file named:

```
.env
```

Add your Groq API Key:

```env
GROQ_API_KEY=your_api_key_here
```

⚠️ Never upload your API key to GitHub.

---

# ▶️ Run Application

Execute:

```bash
python main.py
```

---

# 💻 Example Output

### Input:

```
Enter customer review:

The product quality is excellent and delivery was very fast.
```

### Output:

```
Review Classification:

Positive
```

---

### Another Example:

Input:

```
The product is okay, nothing special.
```

Output:

```
Neutral
```

---

# 🧠 Prompt Engineering Approach

The model is instructed with clear rules:

✅ Analyze customer emotion  
✅ Understand overall meaning  
✅ Return only sentiment category  
✅ Avoid unnecessary explanations  

Example Prompt:

```
Classify the customer review into:
1. Positive
2. Neutral
3. Negative

Return only one category name.
```

---

# 📌 Learning Outcomes

🎯 Understanding Large Language Models (LLMs)  
🎯 Working with Groq API  
🎯 Implementing Prompt Engineering  
🎯 Building AI-based text classification systems  
🎯 Managing API keys securely  

---

# 🔮 Future Enhancements

🚀 Add Web Interface using Streamlit  
🚀 Store reviews in Database  
🚀 Generate sentiment analytics dashboard  
🚀 Support multiple languages  
🚀 Add Batch Review Processing  

---

# 👨‍💻 Author

**Jonnadula Naga Samba Siva Rao**

⭐ If you like this project, give it a star!

```
⭐ AI + Python + LLM = Intelligent Applications 🚀
```

---
