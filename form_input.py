import requests
import os
from dotenv import load_dotenv

load_dotenv() 

CMRA_FORM_ID = 'SKFDhMKo'

def retrieve_form_responses():
    """
    Retrieves all CMRA form responses from Typeform.
    
    Returns:
        list: A list of dictionaries containing the form responses.
    """
    # Placeholder for database retrieval logic
    # This should connect to the database and fetch the backlog form responses
    responses = [
        {"id": 1, "response": "Response 1"},
        {"id": 2, "response": "Response 2"},
        {"id": 3, "response": "Response 3"},
    ]

    access_token = os.getenv('TYPEFORM_PERSONAL_ACCESS_TOKEN')
    get_all_responses_url = f'https://api.typeform.com/forms/{CMRA_FORM_ID}/responses'
    headers = {"Authorization": f"Bearer {access_token}"}
    responses = requests.get(get_all_responses_url, headers=headers)


    return responses.json()

if __name__ == "__main__":
    responses = retrieve_form_responses()
    print(responses)