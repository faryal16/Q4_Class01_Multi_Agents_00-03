import os
import requests
from dotenv import load_dotenv

load_dotenv()

print("\n\t\t>>> Preparing to call OpenRouter API")

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    print("\n❌ ERROR: OPENROUTER_API_KEY not set in environment variables.")
    exit()

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

user_message = "Hello from Faryal Junaid!"

data = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": user_message}
    ]
}

print("\n>>> Sending request to OpenRouter....")
print(f"\t🧑 You: {user_message}")

response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)

print("\n>>> Received response from OpenRouter:")
assistant_reply = response.json()["choices"][0]["message"]["content"]
print(f"\t🤖 Assistant: {assistant_reply}")
