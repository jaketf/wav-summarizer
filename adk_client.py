from google.ai.generativelanguage import TextServiceClient
from google.ai.generativelanguage.types import GenerateTextRequest
from settings import SETTINGS
import json

def summarize_transcription(text: str):
    """
    Calls Google ADK (Generative AI SDK) to generate:
    - summary
    - techniques
    - suggested title
    """

    client = TextServiceClient()

    prompt = f"""
    You are an expert meditation instructor. 
    Given the following meditation transcription, provide:

    1. A concise summary (1-2 sentences)
    2. Key techniques mentioned
    3. Suggested title for this meditation

    Respond in JSON format with keys: summary, techniques, title

    Transcription:
    {text}
    """

    request = GenerateTextRequest(
        model=SETTINGS.ADK_MODEL,
        prompt=prompt,
        max_output_tokens=512,
    )

    response = client.generate_text(request=request)
    generated_text = response.candidates[0].output.strip()

    try:
        result = json.loads(generated_text)
        summary = result.get("summary", "")
        techniques = result.get("techniques", "")
        title = result.get("title", "")
    except Exception as e:
        print(f"ADK JSON parse failed: {e}")
        summary = ""
        techniques = ""
        title = ""

    return summary, techniques, title

