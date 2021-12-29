# import requests
from requests.exceptions import HTTPError

# response = requests.get('https://api.github.com')

# print(type(response))

# print(response.status_code)

# if response.status_code == 200:
#     print('successfull')
# elif response.status_code == 404:
#     print('Not Found.')

# if response:
#     print('successfull')
# elif response.status_code == 404:
#     print('Not Found.')
# else:
#     print('other things')


# try:
#     response = requests.get('https://api.github.com')
# except Exception as ex:
#     print(ex)


# def send_request(adreses, method=None):
#     for url in url_adreses:
#         try:
#             response = requests.get(url)
#             response.raise_for_status()
#         except HTTPError as hterr:
#             print(hterr)
#         except Exception as ex:
#             print(ex)
#         else:
#             print('success')
#         finally:
#             print('always')
#
#
# url_adreses = ['https://api.github.com', 'https://api.github.com/harchi']
#
# send_request(url_adreses)


# response = requests.get('https://api.github.com/search/repositories',
#                         params={'q': 'requests+language:python'})
# j_response = response.json()
# all_repo = j_response['items'][0]
# print(all_repo['name'])

# response = requests.post('https://httpbin.org/post', data={'key': 10})
# response = requests.put('https://httpbin.org/put', data={'key': 10})
# response = requests.delete('https://httpbin.org/delete')
# response = requests.head('https://httpbin.org/get')
# response = requests.patch('https://httpbin.org/post', data={'key': 10})

# print('ok')

# response = requests.post('https://httpbin.org/post', data={'key': 10})
# # response = requests.post('https://httpbin.org/post', data=[('key', 10)])
# j_response = response.json()
# print(j_response)

# from getpass import getpass
#
# response = requests.get('https://api.github.com/user', auth=('hoomanjb', getpass()))
#
# print(response)

# response = requests.get('https://api.github.com' , timeout=100)
# ---------------------------------------
# pandas

# import requests
#
# download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
# target_csv_path = "nba_all_elo.csv"
#
# response = requests.get(download_url)
# response.raise_for_status()    # Check that the request was successful
# with open(target_csv_path, "wb") as f:
#     f.write(response.content)
# print("Download ready.")

import pandas as pd
# import matplotlib

# data = pd.read_csv('nba_all_elo.csv')
# data.head()
# data.tail()
# print(data.info())
# print(data.describe())
# print(type(data))
# print(data["team_id"].value_counts())
# print(data['fran_id'].value_counts())
# print(data.loc[data["fran_id"] == "Lakers", "opp_fran"].value_counts())


# city_number = pd.Series([111, 222, 333], index=['tehran', 'alborz', 'gilan'])
# city_count = pd.Series({'tehran': 21, 'alborz': 26})
# #
# # if 'tehran' in data:
# #     print('ok')
# #
# # print(data)
#
# data = pd.DataFrame({
#     "numbers": city_number,
#     "count": city_count
# })
# print(city_number['tehran'])
# print(city_number[0])
# print(city_number[-1])
# print(city_number[1:])
# print(city_number['tehran':])


# colors = pd.Series(
#     ['red', 'black', 'blue', 'green', 'orange'],
#     index=[1, 2, 3, 5, 8]
# )
# print(colors)
# print(colors.loc[1]) # lable index
# print(colors.iloc[1]) # positional index
# print(colors.iloc[1:3])
# print(colors.iloc[1:3])
# print(colors.iloc[-2])
# print(colors.loc[-2])


# toys = pd.DataFrame([
#     {'name': 'ball', "shape": "sphere"},
#     {"name": "rubik", "shape": "cube"}
# ])
#
city_number = pd.Series([111, 222, 333], index=['tehran', 'alborz', 'gilan'])
city_count = pd.Series({'tehran': 21, 'alborz': 26})

data = pd.DataFrame({
    "numbers": city_number,
    "count": city_count
})
# print(data)
# print(data.loc['tehran'])
# print(data.iloc[1])


data_frame = pd.read_csv('nba_all_elo.csv')
# a = data_frame[data_frame['year_id'] > 2010]
# a = data_frame[data_frame['notes'].notnull()]

print(data_frame.shape)
a = data_frame.dropna()
print(a.shape)
