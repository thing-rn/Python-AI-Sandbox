# ai_automatiom.py

import os
from openai import OpenAI, RateLimitError
from pathlib import Path
from dotenv import load_dotenv

# Project root: .../pythonSBox
project_root = Path(__file__).resolve().parent.parent
load_dotenv(project_root / ".env")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env")

# Read the key from .env and store it in a variable named "client"
client = OpenAI(api_key=api_key)

def summarize(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Summarize the text concisely."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content
    except RateLimitError:
        raise SystemExit(
            "OpenAI request failed: it looks like your account is out of credits or the quota has been exhausted. "
            "Please check your OpenAI billing/usage settings and try again."
        )

if __name__ == "__main__":
    user_text = input("Enter text to summarize: ")
    print("\nSummary:\n", summarize(user_text))
