from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)


def run_incident(prompt: str) -> str:
    """
    Temporary SentinelAI runner.

    Currently sends the prompt directly to Gemini.

    Later this function will execute the
    ADK Incident Commander Agent.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text