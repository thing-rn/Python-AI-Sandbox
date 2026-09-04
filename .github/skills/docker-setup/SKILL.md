---
name: docker-setup
description: "Use when setting up Python Docker containers or integrating Python applications with Ollama or OpenAI APIs. Covers Docker setup, local model connections, hosted API configuration, and troubleshooting."
---

# Docker Setup

1. Check Docker installation with `docker --version`.
2. Create a Dockerfile with a Python base image.
3. Build the image with `docker build -t python_dev .`.
4. Run the container interactively with `docker run -it python_dev bash`.

# AI Integration

## Ollama

Use Ollama for local models without an API key.

1. Confirm Ollama is installed with `ollama --version`.
2. Start the service with `ollama serve` when it is not already running.
3. Download a model, for example `ollama pull llama3.2`.
4. Verify installed models with `ollama list`.
5. Connect through Ollama's OpenAI-compatible endpoint:

```python
import os

from openai import OpenAI

client = OpenAI(
		base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
		api_key="ollama",
)

response = client.chat.completions.create(
		model=os.getenv("OLLAMA_MODEL", "llama3.2"),
		messages=[{"role": "user", "content": "Hello"}],
)
print(response.choices[0].message.content)
```

If the connection fails, check that port `11434` is listening and that the
model name exactly matches the output of `ollama list`.

## OpenAI

Use OpenAI's hosted API with an API key stored outside source code.

1. Install the Python client with `pip install openai`.
2. Set `OPENAI_API_KEY` in the environment or a local `.env` file.
3. Load the key through the client or `python-dotenv`; never commit the key.
4. Handle authentication, connection, and quota errors with clear messages.

```python
import os

from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.chat.completions.create(
		model="gpt-4o-mini",
		messages=[{"role": "user", "content": "Hello"}],
)
print(response.choices[0].message.content)
```

For a `429` error with `insufficient_quota` or
`credit_balance_exhausted`, check the account billing and usage limits. Do not
retry repeatedly because quota errors are not fixed by waiting.

## Provider Selection

- Prefer Ollama when privacy, offline use, or no API cost is required.
- Prefer OpenAI when hosted models, simple deployment, or higher capability is
	required.
- Keep the provider and model configurable with environment variables when an
	application may use either service.
