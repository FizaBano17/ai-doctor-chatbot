
# chat.py 
import requests
import os
from dotenv import load_dotenv

load_dotenv()
OR_KEY = os.getenv("OPENROUTER_API_KEY")

def medical_chat(message):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OR_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://localhost",
        "X-Title": "AI Doctor Assistant"
    }

    payload = {
        "model": "deepseek/deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a medical expert. Give clear advice."},
            {"role": "user", "content": message}
        ]
    }

    r = requests.post(url, json=payload, headers=headers)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]


print("Loaded KEY:", OR_KEY)

