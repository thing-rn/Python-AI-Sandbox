import os
from openai import APIConnectionError, OpenAI

client = OpenAI(
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
    api_key="ollama",
)
model = os.getenv("OLLAMA_MODEL", "llama3.2")

def summarize(text):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Summarize the text concisely."},
                {"role": "user", "content": text},
            ],
        )
        return response.choices[0].message.content
    except APIConnectionError:
        raise SystemExit(
            "Could not connect to Ollama. Start it with 'ollama serve' and "
            f"make sure the '{model}' model is installed."
        )

if __name__ == "__main__":
    user_text = input("Enter text to summarize: ")
    print("\nSummary:\n", summarize(user_text))
