from flask import Flask, request

from form_response_module import retrieve_form_responses

app = Flask(__name__)


@app.route("/backlog-reports", methods=["GET"])
def generate_backlog_reports():
    responses = retrieve_form_responses()
    return {"responses": responses}


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Webhook received:", data)
    # Process the webhook data as needed
    return {"status": "success"}
