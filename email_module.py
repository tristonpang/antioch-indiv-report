import base64
import mimetypes
import os.path
from email import policy
from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.addons.current.action.compose",
    "https://www.googleapis.com/auth/gmail.send",
]


def set_creds():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except:
                print("Failed to refresh credentials, re-authenticating...")
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds


def gmail_send_message(recipient_email, report_path):
    """Create and send an email message
    Print the returned  message id
    Returns: Message object, including message id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds = set_creds()

    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage(policy=policy.SMTP.clone(max_line_length=1000))

        message.set_content(
            "Greetings from Antioch21! If you are seeing this, the email's full message failed to load. Please refer to further details in your CMRA Report attached.",
        )

        message.add_alternative(
            """\
        <html>
        <body>
            <p>Greetings from Antioch21!<br><br>
            Thank you for completing the Church Missions Readiness Assessment (CMRA). Attached is your individualized report with your overall readiness score and detailed insights for each domain.<br><br>
            Inside, you’ll find suggested next steps, space for reflection, and prompts to guide discussion with your church leadership or fellow participants. We encourage you to share and compare your reports if others in your church also completed the CMRA.<br><br>
            If you’d like to process your results or explore ways to grow in missions readiness, we’d be glad to connect - just reach out at <a href="mailto:admin@antioch21.sg">admin@antioch21.sg</a>.<br><br>
            Warm regards,<br>
            Darrell Ong<br>
            Director Of Partnerships<br>
            Antioch21
            </p>
        </body>
        </html>
        """,
            subtype="html",
        )

        message["To"] = recipient_email
        message["From"] = "tristondevelopment@gmail.com"
        message["Subject"] = (
            "Your CMRA Report - A Snapshot of Your Church’s Missions Readiness"
        )

        # Attach report
        type_subtype, _ = mimetypes.guess_type(report_path)
        maintype, subtype = type_subtype.split("/")

        with open(report_path, "rb") as fp:
            attachment_data = fp.read()
            message.add_attachment(
                attachment_data, maintype, subtype, filename="CMRA_Report.pdf"
            )

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}
        # pylint: disable=E1101
        send_message = (
            service.users().messages().send(userId="me", body=create_message).execute()
        )
        print(f"Message Id: {send_message['id']}")
    except HttpError as error:
        print(f"An error occurred: {error}")
        send_message = None
    return send_message


if __name__ == "__main__":
    gmail_send_message()
