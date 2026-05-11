import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_summary(context):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=context
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"