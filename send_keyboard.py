import requests
import os
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
text = 'Keyboard '
button = {   
        'text': 'Button 1'
        }
button1 = {   
        'text': 'Button 2'
        }
button2 = {   
        'text': 'Button 3'
        }
keyboard = [[button,button1,button2]]
reply_keyboard = {
    'keyboard': keyboard
}

# print(send_message(chat_id, text,reply_keyboard))


