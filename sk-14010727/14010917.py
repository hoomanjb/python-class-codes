import sqlite3
from sqlite3 import Error

import psycopg2
from psycopg2 import OperationalError

# Auto increment

def create_connection(path='test.db'):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('connection was Success')
    except Error as err:
        print(f'somthing is wrong and error is: {err}')
    return connection

# lite_connection = create_connection()

def pg_create_connection(db_host, db_user, db_password, db_port, db_name):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name, user=db_user, password=db_password,
            host=db_host, port=db_port)
        print('ok')
    except OperationalError as ex:
        print(f'error: {ex}')
    return connection


lite_connection = create_connection()
pg_connection = pg_create_connection(
    db_host='localhost', db_port=5432, db_password='1234qwer',
    db_name='test', db_user='postgres'
)

# in function bara connection haye postgres
# def create_database(connection, query):
#     connection.autocommit = True
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print('ok')
#     except OperationalError as ex:
#         print(ex)
#
# query = 'CREATE DATABASE TEST'
# create_database(pg_connection, query)

def run_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('ok')
    except OperationalError as err:
        print(err)
    except Error as errrr:
        print(errrr)


crete_table_users = '''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT ,
    national_code TEXT 
);
'''

crete_table_posts = '''
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    user_id INTEGER NOT NULL ,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
'''

create_table_comments = """
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY,
    text TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (post_id) REFERENCES posts (id)
    );
"""

create_table_likes = """
CREATE TABLE IF NOT EXISTS likes (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (post_id) REFERENCES posts (id)
    );
"""

# run_query(lite_connection, query=crete_table_users)
# run_query(pg_connection, query=crete_table_users)
#
# run_query(lite_connection, query=crete_table_posts)
# run_query(pg_connection, query=crete_table_posts)
#
# run_query(lite_connection, query=create_table_comments)
# run_query(pg_connection, query=create_table_comments)
#
# run_query(lite_connection, query=create_table_likes)
# run_query(pg_connection, query=create_table_likes)

create_insert_user = '''
    INSERT INTO 
    users 
        (name, age, gender, national_Code)
    VALUES
        ('hooman2', 20, 'male', '123123'),
        ('hooman3', 30, 'male', '789789'),
        ('hooman4', 40, 'male', '456456')
'''

insert_post = '''
    INSERT INTO
    posts
        (title, description, user_id)
    VALUES
        ('t1', 'desc1', 1),
        ('t2', 'decs2', 3)
'''

# run_query(pg_connection, create_insert_user)

# run_query(pg_connection, insert_post)

def get_data(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except OperationalError as err:
        print(err)
    except Error as errrr:
        print(errrr)
    return result

# get_all_users = '''
#     SELECT * FROM users where age > 30
# '''
#
# a = get_data(pg_connection, get_all_users)
# print(a)

# get_users_post = '''
#     SELECT users.name FROM posts
#     INNER JOIN users on users.id = posts.user_id
# '''
#
# a = get_data(pg_connection, get_users_post)
# print(a)


def update_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except OperationalError as err:
        print(err)
    except Error as errrr:
        print(errrr)


update_user = '''
    UPDATE users
    set age = 99, name='taghi'
    where id = 1
'''
update_query(pg_connection, update_user)

