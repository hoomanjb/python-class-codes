import requests
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
# target = 'nba_all_data.csv'
#
# response = requests.get(download_url)
# response.raise_for_status() # 500 error server, 400 error client, 200 success
#
# with open(target, 'wb') as f:
#     f.write(response.content)
#
# print('download ready.')

# pd.set_option('display.max.columns', 5)
# pd.set_option('display.precision', 3)

df = pd.read_csv('nba_all_data.csv')

# print(type(df))
# print(len(df))
# print(df.shape)
# print(df.head(10))
# print(df.tail(10))

# print(df.info())

# print(df['pts'].describe())

# print(df['team_id'].value_counts())
# print(df['fran_id'].value_counts())

# print(df.loc[df['fran_id'] == 'Lakers', "team_id"].value_counts())

df['date_played'] = pd.to_datetime(df['date_game'])

# print(df.loc[df['team_id'] == 'MNL', 'date_played'].agg(('min', 'max')))

# a = pd.Series([5555, 7000, 1900])
# print(a)
# print(a.values)
# print(a.index)

city_name = pd.Series(
    [5555, 7000, 1900],
    index=['tehran', 'karaj', 'shiraz']
)
city_count = pd.Series({'tehran': 5, 'shiraz': 8})

city = pd.DataFrame({
    "city_name": city_name,
    "city_count": city_count
})
# print(city)
# print(city['tehran'])

# print(city_name)
# print(city_name['tehran'])
# print(city_name[0])

colors = pd.Series(
    ['red', 'orange', 'purple', 'green'],
    index=[1, 7, 5, 8]
)

# print(colors)
# print(colors.loc[1])
# print(colors.iloc[1])
# print(colors.iloc[-1])

toys = pd.DataFrame([
    {'name': 'ball', 'shape': 'sphere'},
    {'name': 'rubik', 'shape': 'cube'}
])

# print(toys)
# print(toys.shape)

# print(toys['name'].loc[])

a = df[df['year_id'] > 2011]
# print(a)

b = df[df['notes'].notnull()]
# print(b)

c = df[df['fran_id'].str.endswith('ers')]
# print(c)

d = df[
    (df['_iscopy'] == 0) &
    (df['pts'] > 100) &
    (df['team_id'] == 'BLB')
]
# print(d)

# e = df['pts']
# print(e.sum())

# print(df.groupby('fran_id')['pts'].sum())


# print(df[
#           (df['fran_id'] == 'Bulls') &
#           (df['year_id'] > 2010)
#       ].groupby(['year_id', 'game_result'])['game_id'].count())

g = df[
    (df['fran_id'] == 'Bulls') &
        (df['year_id'] > 2010)
      ].groupby(['year_id', 'game_result'])['game_id'].count()

# print(type(g))
# g = g.cumsum()
# plt.figure()
# g.plot()
# plt.show()


df = pd.DataFrame({
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','M','M','F','M'],
    'state':['california','dc','california','dc','california','texas','texas'],
    'num_children':[2,0,0,3,2,1,4],
    'num_pets':[5,1,0,5,2,2,3]
})

# df.plot(kind='bar',x='name',y='age')

ax = plt.gca()

# df.plot(kind='line',x='name',y='num_children',ax=ax)
# df.plot(kind='line',x='name',y='num_pets', color='red', ax=ax)

# plt.savefig('output.png')

df.groupby('state')['name'].nunique().plot(kind='bar')

plt.show()


