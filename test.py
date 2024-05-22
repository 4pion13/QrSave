import requests
import json
import webbrowser

webbrowser.open_new('https://oauth.yandex.ru/authorize?response_type=code&client_id=333dd64379b14ae8a2112911b5b2b416')

code = input("Code: ")

res = requests.post('https://oauth.yandex.ru/token', data={'grant_type': 'authorization_code', 'code': code})
print(res.text)