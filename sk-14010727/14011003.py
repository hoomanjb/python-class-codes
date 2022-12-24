
# test.com/users
import requests
#
# response = requests.get('https://divar.ir/s/tehran/car/peugeot/206/2?color=%D8%B3%D9%81%DB%8C%D8%AF')
# print(response)
# response = requests.get('test.com/companies/foolad/today')

# users  - crud
# create -> user add
# read -> get - users/  - users/5
# update  -> post -  users/5
# delete -> users


# ###################################

# url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
new_file = 'nab_all_data.csv'
#
# response = requests.get(url)
# response.raise_for_status()
#
# with open(new_file, 'wb') as f:
#     f.write(response.content)


# f = open('test.txt', 'w')
# f.write('salam chetori')
# print(f)
# f.close()

import pandas as pd

df = pd.read_csv(new_file)
# print(df)
# print(df.shape)
# print(df.head())
# print(df.info())

# print(df.describe())
# print(df['team_id'].value_counts())

# print(df['fran_id'].value_counts())

# print(df.loc[df['fran_id'] == 'Lakers', 'team_id'].value_counts())

# df['date_played'] = pd.to_datetime(df['date_game'])
#
# print(df.loc[df['team_id'] == 'MNL', 'date_played'].min())
# print(df.loc[df['team_id'] == 'MNL', 'date_played'].max())

data = {'name': ['test', 'hooman', 'test2', 'test3'],
        'city': ['tehran', 'karaj', 'rasht', 'yazd'],
        'age': [2, 3, 5, 6]
}
# row_index = ['a', 'b', 'c', 'd']

df = pd.DataFrame(data=data)
# print(df)
# print(df['age'])
# print(df.age)
a = df['age']
print(a[3])