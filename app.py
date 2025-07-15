from flask import Flask, request

from form_response_module import parse_raw_response, retrieve_form_responses
from report_module import generate_report_markdown

app = Flask(__name__)


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

    # TODO: send email for each report

    # Process the webhook data as needed
    return {"status": "success"}
