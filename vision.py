# vision.py - Using OpenRouter Vision Model
import base64
import os
import requests
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("OPENROUTER_API_KEY")

def analyze_image(image_path):
    if not KEY:
        return "OpenRouter API key not found! Add it in .env as OPENROUTER_API_KEY=..."

    # Convert image → base64
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json"
    }

    # Best FREE vision model on OpenRouter
    payload = {
        "model": "meta-llama/llama-3.2-90b-vision-instruct",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Analyze this skin/face image for acne or other issues. Provide cause + next steps."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded}"
                        }
                    }
                ]
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Throw error if API returns 400/401/429 etc.

    return response.json()["choices"][0]["message"]["content"]



