import requests
import os
TOKEN = os.environ['TOKEN'] 

def send_location(chat_id: int, latitude: float, longitude: float):
   
    URL = f'https://api.telegram.org/bot{TOKEN}/sendLocation'
    response = requests.get(URL, params={'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude})
    return response.json()


def send_venue(chat_id: int, latitude: float, longitude: float, title: str, address: str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendVenue'
    response = requests.get(URL, params={'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude, 'title': title, 'address': address})
    return response.json()


chat_id = 5423257804
latitude = 40.7128
longitude = -74.0060
title = 'Home'
address = 'New York'

send_venue(chat_id, latitude, longitude, title, address)

