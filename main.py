import base64
from google.cloud import storage
from settings import SETTINGS
from speech_client import transcribe_wav
from adk_client import summarize_transcription
from sheets_client import write_to_sheet, ensure_sheet_exists

def gcs_trigger(event, context):
    bucket_name = event['bucket']
    file_name = event['name']

    if not file_name.lower().endswith(".wav"):
        print(f"Skipping {file_name}, not a WAV")
        return

    print(f"Processing {file_name} from {bucket_name}")

    # Download WAV
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    audio_bytes = blob.download_as_bytes()

    # Transcription
    transcription_text = transcribe_wav(audio_bytes)

    # ADK summarization
    summary, techniques, title = summarize_transcription(transcription_text)

    # Ensure sheet exists
    ensure_sheet_exists(SETTINGS.SHEET_NAME)

    # Write to sheet
    write_to_sheet(
        filename=file_name,
        transcription=transcription_text,
        summary=summary,
        techniques=techniques,
        title=title,
        model=SETTINGS.ADK_MODEL
    )

    print(f"Completed processing {file_name}")

