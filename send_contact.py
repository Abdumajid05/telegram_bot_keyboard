import requests
import os
from pprint import pprint
TOKEN = os.environ['TOKEN'] 

def send_contact(chat_id: int, phone_number: str, first_name: str, last_name: str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendContact'
    response = requests.get(URL, params={'chat_id': chat_id, 'phone_number': phone_number, 'first_name': first_name, 'last_name': last_name})
    return response.json()


chat_id = 5423257804
phone_number = '+32187382738'
first_name = 'Abdumajid'
last_name = 'Abdulazizov'


pprint(send_contact(chat_id, phone_number, first_name, last_name))