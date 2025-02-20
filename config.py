import openai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Make sure OPENAI_API_KEY is set.")

client = openai.OpenAI(api_key=api_key)