import requests
import os
from send_contact import send_contact
from send_location import send_location
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

def send_message(chat_id: int, text: str,reply_keyboard: list):
   
    response = requests.post(URL, json={
        'chat_id': chat_id, 
        'text': text,
        'reply_markup':reply_keyboard 
        })
    return response.json()

chat_id = 5423257804
text = 'Keyboard'
button = {   
        'text': 'Contact',
        'request_contact': True,
        'send_contact': send_contact
        
        }
button1 = {   
        'text': 'Location',
        'request_location': True,
        'send_location': send_location
        
        }
# button2 = {   
#         'text': 'Button 3'
#         }
keyboard = [[button,button1]]
reply_keyboard = {
    'keyboard': keyboard
}

# print(send_message(chat_id, text,reply_keyboard))


