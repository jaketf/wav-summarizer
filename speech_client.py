from google.cloud import speech
from settings import SETTINGS

def transcribe_wav(audio_bytes: bytes) -> str:
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=audio_bytes)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=SETTINGS.SAMPLE_RATE_HZ,
        language_code="en-US",
    )
    response = client.recognize(config=config, audio=audio)
    return " ".join([result.alternatives[0].transcript for result in response.results])

