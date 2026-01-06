import json
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from email_module import gmail_send_message
from form_response_module import parse_raw_response
from report_module import (
    generate_report_markdown,
)

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build("gmail", "v1", credentials=creds)
        results = service.users().labels().list(userId="me").execute()
        labels = results.get("labels", [])

        if not labels:
            print("No labels found.")
            return
        print("Labels:")
        for label in labels:
            print(label["name"])

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")


def test_report_generation():
    with open("example-webhook-response.json", "r") as file:
        data = json.load(file)
        form_response = parse_raw_response(data["form_response"])
        report_path = generate_report_markdown(form_response)
        gmail_send_message("pang.triston@gmail.com", report_path)


def generate_backlogged_reports():
    with open("input-responses.json", "r") as file:
        data = json.load(file)
        for raw_response in data["items"]:
            form_response = parse_raw_response(raw_response)
            report_path = generate_report_markdown(form_response)
            gmail_send_message(form_response.answers.email, report_path)
            print(f"Processed report for {form_response.answers.email}")


if __name__ == "__main__":
    # main()
    # test_report_generation()
    generate_backlogged_reports()
