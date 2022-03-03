# sqllite3 , postgres, mysql, oracle,
# mongodb, {'name': pirahan, }  {'name': Tv, 'size':}

import sqlite3
from sqlite3 import Error

import psycopg2 # psycopg2-binary
from psycopg2 import OperationalError


# SQLITE
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path) # test.sqlite
        print('connection success')
    except Error as e:
        print(f'error is: {e}')

    return connection


# postgres
def pg_create_connection(db_host, db_user, db_password, db_port, db_name):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name, user=db_user, password=db_password,
            host=db_host, port=db_port)
        print('connection success')
    except OperationalError as e:
        print(f'error is: {e}')

    return connection

# sql_connection = create_connection('test.db')
#
# pg_connection = pg_create_connection(
#     db_host='localhost', db_name='postgres',
#     db_port=5432, db_password='1234qwer', db_user='postgres')


# def pg_create_database(connection, query):
#     connection.autocommit = True
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print('query success')
#     except OperationalError as e:
#         print(f'error is {e}')


# create_db_query = 'CREATE DATABASE new_app'
#
# pg_create_database(pg_connection, create_db_query)

def run_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('query success')
    except OperationalError as e:
        print(f'error is {e}')
    except Error as err:
        print(f'error is {err}')

create_table_users = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    nationality TEXT
    );
"""

create_table_posts = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
    );
"""

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

create_insert_user = """
    INSERT INTO
        users (name, age, gender, nationality)
    VALUES 
        ('hooman', 15, 'male', 'ir'),
        ('ali', 30, 'male', 'usa'),
        ('zahra', 20, 'female', 'ir')
;"""

pg_create_insert = """
    INSERT INTO
        comments (id, text, user_id, post_id)
    VALUES 
        (1, 'yechi', 1, 1),
        (2, 'yechi2', 3, 2),
        (3, 'yechi3', 2, 3)
;"""

lite_create_insert = """
    INSERT INTO
        comments (text, user_id, post_id)
    VALUES 
        ('yechi', 1, 1),
        ('yechi2', 3, 2),
        ('yechi3', 2, 3)
;"""

pg_create_likes = """
INSERT INTO
  likes (id,user_id, post_id)
VALUES
  (1, 1, 1),
  (2, 2, 3),
  (3, 1, 2),
  (4, 1, 3),
  (5, 2, 1),
  (6, 2, 2),
  (7,1, 3);
"""

lite_create_likes = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (1, 1),
  (2, 3),
  (1, 2),
  (1, 3),
  (2, 1),
  (2, 2),
  (1, 3);
"""

# run_query(pg_connection, pg_create_likes)
# run_query(sql_connection, lite_create_likes)

def select_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f'error is {e}')
    except Error as err:
        print(f'error is {err}')

# select_users = "SELECT * FROM users" #posts , likes, comments
# users = select_query(pg_connection, select_users)
# for user in users:
#     print(user)

# select_users_posts = """
# SELECT
#     users.id,
#     users.name,
#     posts.description
# FROM
#     posts
#     INNER JOIN users ON users.id = posts.id
# """
#
# users = select_query(pg_connection, select_users_posts)
# for user in users:
#     print(user)
#
# def update_query(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()
#     except OperationalError as e:
#         print(e)
#
# update_post = """
# UPDATE
#     posts
# SET
#     description = 'yechi5'
# WHERE
#     id = 2
# """

# update_query(pg_connection, update_post)

# ---------------------------------------------
# 09121236547 test
# text = 'hello123world'

import re

# a = re.search('123', text)
# if re.search('456', text):
#     print('123 found')
# else:
#     print('123 not found')
text = 'hello123world'
# a = re.search('[0-9][0-9][0-9]', 'asd12a3')
# a = re.search('^1.3$', '1v3')
# a = re.search('1*3', '13')
# a = re.search('1+3', '13')
# a = re.search('1?3', 'asd3asd')
# a = re.search('llo[4-5]', text)
# a = re.search('[a-z]', '123a')
# a = re.search('[a-z][a-z]', '123ab')
# a = re.search('[0-9a-fA-F]', 'z')
# a = re.search('[^0-9]', 'asd')
a = re.search('[-abc]', '123f')


print(a)


# select join passw email