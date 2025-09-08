from flask import Flask, request

from dev_test import test_report_generation
from email_module import gmail_send_message
from form_response_module import parse_raw_response, retrieve_form_responses
from report_module import clean_up_report, generate_report_markdown

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Welcome to the Antioch21 Report Generator!"


@app.route("/backlog-reports", methods=["GET"])
def generate_backlog_reports():
    responses = retrieve_form_responses()
    return {"responses": responses}


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Webhook received:", data["event_id"])
    # Parse into domain object
    form_response = parse_raw_response(data["form_response"])

    # Generate report for each response
    report = generate_report_markdown(form_response)

    # Send email for each report
    gmail_send_message(form_response.answers.email, report)

    clean_up_report(report)

    # Process the webhook data as needed
    return {"status": "success"}


@app.route("/test-email", methods=["GET"])
def test_email():
    test_report_generation()
    return {"status": "email sent"}
