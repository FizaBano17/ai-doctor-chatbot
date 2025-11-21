# 🩺 AI Doctor Bot (Text + Voice + Image)

A simple AI-powered medical assistant that can:

✅ Answer medical questions (Text)  
✅ Take voice input and convert it to medical advice  
✅ Analyze uploaded images (ex: acne, skin issues)

This project uses:
- **OpenRouter API** for text chat (OpenAI-like models)
- **Groq Vision Models** (or OpenRouter Vision) for image analysis
- **Python SpeechRecognition** + **sounddevice** for voice
- **Gradio** for UI (optional)

---

## 📂 Project Structure

ai_doctor_voicebot/
│
├── doctor.py # CLI main program
├── chat.py # Text medical chatbot (OpenRouter)
├── vision.py # Image diagnosis (Vision model)
├── speech.py # Voice recording + transcription
├── ai_doctor_ui.py # Gradio web UI
├── .env # API keys
└── requirements.txt

---

## 🚀 Installation

### 1️⃣ Install Python 3.10–3.12  
(Gradio + Pillow do NOT support Python 3.14)

Download from: https://www.python.org/downloads/

---

### 2️⃣ Create Virtual Environment


Activate:

**Windows**

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt


If Gradio fails, install manually:

pip install gradio


---

## 🔑 Environment Variables

Create a `.env` file:

OPENROUTER_API_KEY=your_key_here

---

## ▶️ Run the App (CLI)

Menu:
1 = Text question
2 = Voice question
3 = Image diagnosis

---

## 🌐 Run the Gradio UI

python ai_doctor_ui.py

Your local app opens in the browser.

---

## 📝 Notes

- OpenRouter is used for **medical text responses**
- Vision analysis depends on whichever model you selected  
  (Groq or OpenRouter vision)
- Voice recognition uses Google Web Speech API (free)

---
