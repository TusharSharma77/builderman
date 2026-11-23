from google import genai
from app.core.config import settings

client = genai.Client(api_key=settings.google_api_key)

def generate_text(prompt: str) -> str:
    response = client.models.generate_content(
        model=settings.gemini_model,
        contents=prompt,
    )

    if response.text is None:
        raise RuntimeError("Gemini ne text response nahi diya.")

    return response.text