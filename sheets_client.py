import gspread
from google.cloud import secretmanager
from settings import SETTINGS

def get_sheets_client():
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{SETTINGS.GCP_PROJECT}/secrets/{SETTINGS.SHEETS_JSON_SECRET}/versions/latest"
    response = client.access_secret_version(name=name)
    credentials_json = response.payload.data.decode("UTF-8")
    return gspread.service_account_from_dict(eval(credentials_json))

def ensure_sheet_exists(sheet_name: str):
    client = get_sheets_client()
    try:
        client.open(sheet_name)
    except gspread.SpreadsheetNotFound:
        client.create(sheet_name)
        print(f"Created sheet: {sheet_name}")

def write_to_sheet(filename, transcription, summary, techniques, title, model):
    client = get_sheets_client()
    sheet = client.open(SETTINGS.SHEET_NAME).sheet1
    sheet.append_row([filename, transcription, summary, techniques, title, model])

