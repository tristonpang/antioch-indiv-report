import os

import requests
from dotenv import load_dotenv

from interfaces.form_response import FormResponse

load_dotenv()

CMRA_FORM_ID = "SKFDhMKo"
CMRA_WEBHOOK_NAME = "cmra_webhook"


def retrieve_form_responses():
    """
    Retrieves all CMRA form responses from Typeform.

    Returns:
        list: A list of dictionaries containing the form responses.
    """
    access_token = os.getenv("TYPEFORM_PERSONAL_ACCESS_TOKEN")
    get_all_responses_url = f"https://api.typeform.com/forms/{CMRA_FORM_ID}/responses"
    headers = {"Authorization": f"Bearer {access_token}"}
    responses = requests.get(get_all_responses_url, headers=headers)

    return responses.json()


def register_form_webhook():
    """
    Registers a webhook for the CMRA form to receive notifications on new responses.

    Returns:
        dict: The response from the Typeform API.
    """
    access_token = os.getenv("TYPEFORM_PERSONAL_ACCESS_TOKEN")
    register_webhook_url = (
        f"https://api.typeform.com/forms/{CMRA_FORM_ID}/webhooks/{CMRA_WEBHOOK_NAME}"
    )
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    webhook_data = {
        "url": f"{os.getenv('APP_URL')}/webhook",
        "enabled": True,
        "events": ["form_response"],
    }

    response = requests.put(register_webhook_url, headers=headers, json=webhook_data)

    return response.json()


def parse_raw_response(raw_response):
    """
    Parses the raw response from Typeform into a structured format.

    Args:
        raw_response (dict): The raw response data from Typeform.

    Returns:
        FormResponse: An instance of FormResponse containing parsed data.
    """

    return FormResponse(raw_response)


if __name__ == "__main__":
    # responses = retrieve_form_responses()
    # print(responses)

    webhook_response = register_form_webhook()
    print(webhook_response)
