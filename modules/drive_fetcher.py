import os
import io
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import PyPDF2

def get_drive_text(folder_id):
    creds = None
    # 1. Look for existing token to avoid re-authentication
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/drive.readonly'])
    
    # 2. If no valid token, login once
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', ['https://www.googleapis.com/auth/drive.readonly'])
            creds = flow.run_local_server(port=0)
        # Save the token for the next time
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    # Search for the latest file in your Topic folder
    query = f"'{folder_id}' in parents"
    results = service.files().list(q=query, orderBy="modifiedTime desc", pageSize=1, fields="files(id, name, mimeType)").execute()
    items = results.get('files', [])

    if not items:
        print("No files found in Google Drive.")
        return None

    file = items[0]
    print(f"   -> Processing: {file['name']}")
    
    fh = io.BytesIO()
    if file['mimeType'] == 'application/vnd.google-apps.document':
        request = service.files().export_media(fileId=file['id'], mimeType='text/plain')
    else:
        request = service.files().get_media(fileId=file['id'])

    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    
    if file['mimeType'] == 'application/pdf':
        reader = PyPDF2.PdfReader(io.BytesIO(fh.getvalue()))
        return " ".join([page.extract_text() for page in reader.pages])
    return fh.getvalue().decode('utf-8')