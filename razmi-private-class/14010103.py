import sqlite3
import psycopg2


def create_connection_sqlite(path):
    try:
        connection = sqlite3.connect(path)
        print('connection was successfull')
        return connection
    except Exception as ex:
        print('something is wrong')
        print(ex)

def create_connection_postgres(user, password, port, db_name, host='localhost'):
    try:
        # cnt = create_connection('postgresql://{root}:{123}@{172.15.1.1}:{5432}/alaki')
        connection = psycopg2.connect(user=user, database=db_name, password=password, host=host, port=port)
        print('connection was successfull')
        return connection
    except Exception as ex:
        print('something is wrong')
        print(ex)

# cnt = create_connection('postgresql://{root}:{123}@{172.15.1.1}:{5432}/alaki')
# print(cnt_postgres)



cnt_postgres = create_connection_postgres(user='postgres', password='1234qwer', port='5432', db_name='alaki')
cnt_sqlite = create_connection_sqlite('alaki.sql')

cursor_sqlite = cnt_sqlite.cursor()
cursor_postgres = cnt_postgres.cursor()

# query = """
# CREATE TABLE if not exists USER (
#     id integer primary key,
#     first_name text not null,
#     last_name text not null,
#     phone text unique
# );
# """
#
# cursor_sqlite.execute(query)
# cnt_sqlite.commit()
#
#
# query = """
# CREATE TABLE IF NOT EXISTS USERS (
#     id integer primary key,
#     first_name text not null,
#     last_name text not null,
#     phone text unique
# );
# """
# cursor_postgres.execute(query)
# cnt_postgres.commit()
#
# query = """
# insert into
#     user (id, first_name, last_name)
#     values
#      (1, 'hooman', 'javan'),
#      (2, 'mreza', 'razmi')
# ;"""
#
# cursor_sqlite.execute(query)
# cnt_sqlite.commit()

a = ['hooman', 'mreza']
b = ['javan', 'razmi']

query = "insert into user (id, first_name, last_name) values {query} ;"
# result = "(1, 'hooman', 'javan'), (2, 'mreza', 'razmi')"
result = ""
for index, item in enumerate(a, start=1):
    result += f"({index}, '{item}', '{b[index-1]}'),"
print(result)

query.format(query=result)

