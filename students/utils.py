import requests
import os

TOKEN = os.getenv('TOKEN')

URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

CHAT_ID = os.getenv('CHAT_ID')

def telegram_send(message):
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    r = requests.post(URL, data=payload)
    print(r.status_code, r.text)