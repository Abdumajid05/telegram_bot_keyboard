import requests
import os
from pprint import pprint
TOKEN = os.environ['TOKEN'] 


def send_photo(chat_id: int, photo: str):
    
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    response = requests.get(URL, params={'chat_id': chat_id, 'photo': photo})
    return response.json()
chat_id = 5423257804
photo = 'https://nationalpost.com/wp-content/uploads/sites/2/2021/06/GettyImages-1233809100.jpg'
response = send_photo(chat_id, photo)
pprint(response)



