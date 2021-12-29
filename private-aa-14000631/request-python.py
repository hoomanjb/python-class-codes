import requests
# import pandas
from requests.exceptions import HTTPError

# try:
#     response = requests.get("https://api.github.com/user/emails")
# except Exception as e:
#     print(e)
# else:
#     if response.status_code == 200:
#         print('success')
#         print(response.text)
#
#     elif response.status_code == 404:
#         print('page not found!!!')
#     else:
#         print('something wrong')

# for url in ['https://api.github.com', 'https://api.github.com/harchi']:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'ye etefaghi oftade az type {http_err}')
#     except Exception as exc:
#         print(f'wrong {exc}')
#     else:
#         print('successfull')

# for url in ['https://api.github.com', 'https://api.github.com/harchi']:
# try:
#     # response = requests.get('https://api.github.com')
#     response = requests.get(url='https://api.github.com/search/repositories',
#                             params={'q': 'requests+language:python'})
#     response.raise_for_status()
#
# except HTTPError as http_err:
#     print(f'ye etefaghi oftade az type {http_err}')
#
# except Exception as exc:
#     print(f'wrong {exc}')
#
# else:
#     b = response.text
#     c = response.json()
#
#     print('ok')

import json

try:
    response = requests.post(url='https://httpbin.org/post', data=json.dumps({'password': 'value'}))
    response.raise_for_status()

except HTTPError as http_err:
    print(f'ye etefaghi oftade az type {http_err}')

except Exception as exc:
    print(f'wrong {exc}')

else:
    b = response.text
    c = response.json()

    print('ok')