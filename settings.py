from pydantic import BaseSettings

class Settings(BaseSettings):
    GCP_PROJECT: str
    SHEET_NAME: str = "Meditation Transcripts"
    SHEETS_JSON_SECRET: str
    ADK_MODEL: str = "models/text-bison-001"
    MAX_CHUNK_SECONDS: int = 600
    SAMPLE_RATE_HZ: int = 44100
    TRANSCRIBE_TIMEOUT: int = 600

    class Config:
        env_file = ".env"

SETTINGS = Settings()

