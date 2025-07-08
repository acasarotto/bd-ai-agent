import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not found")

# Create the client
client = genai.Client(api_key=api_key)

# Generate text with Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",  # or "gemini-pro"
    contents="Say something witty about Python."
)
print(response.text)
