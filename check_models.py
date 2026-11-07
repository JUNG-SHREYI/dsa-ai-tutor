import os

from dotenv import load_dotenv
from google import genai

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Gemini API key not found in environment or .env file")

client = genai.Client(api_key=api_key)

for model in client.models.list():
    if "generateContent" in (model.supported_actions or []):
        print(model.name)