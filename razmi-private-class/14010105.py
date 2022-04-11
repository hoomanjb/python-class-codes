import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query, is_many=False, values=None):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        if is_many:
            cursor.executemany(insert_likes2, values)
        else:
            cursor.execute(query, values)
        print('query executed successfully')
    except Exception as ex:
        print(ex)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as ex:
        print(ex)


create_table_users = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
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
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

create_table_like = """
CREATE TABLE IF NOT EXISTS likes (
    id INTEGER PRIMARY KEY,
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

connection = create_connection('alaki', 'postgres', '1234qwer', 'localhost', '5432')
# execute_query(connection, create_table_users)
# execute_query(connection, create_table_posts)
# execute_query(connection, create_table_comments)
# execute_query(connection, create_table_like)

insert_users = """
INSERT INTO 
    users (name, age, gender, nationality)
VALUES 
    ('hooman', 30, 'male', 'IR'),
    ('mreza', 32, 'male', 'IR'),
    ('zahra', 15, 'female', 'IR'),
    ('pooya', 20, 'male', 'IR')
;"""

# execute_query(connection=connection, query=insert_users)

insert_posts = """
INSERT INTO 
    posts (title, description, user_id)
VALUES
    ('HELP', 'yechiziiiii', 1),
    ('HELP2', 'yechiziiiii2', 2),
    ('HELP3', 'yechiziiiii3', 2),
    ('HELP4', 'yechiziiiii4', 3)
;"""

# execute_query(connection=connection, query=insert_posts)

insert_comments = """
INSERT INTO 
    comments (text, user_id, post_id)
VALUES
    ('Warning', 1, 1),
    ('Warning2', 1, 2),
    ('Warning3', 2, 2),
    ('Warning4', 3, 3)
;"""

insert_likes = """
INSERT INTO 
    likes (user_id, post_id)
VALUES
    (1 ,1),
    (2, 2),
    (3, 2),
    (1, 3)
;"""

# execute_query(connection=connection, query=insert_comments)
# execute_query(connection=connection, query=insert_likes)

insert_likes2 = "INSERT INTO likes (user_id, post_id) VALUES ( %s, %s )"
values = [(1, 3), (2, 3)]

# execute_query(connection=connection, query=insert_likes2, is_many=True, values=values)

users = [
    ("ali", 12, "male", "USA"),
    ("taghi", 18, "male", "USA"),
    ("reza", 17, "male", "IR"),
    ("parham", 8, "male", "USA"),
]

user_records = ", ".join(["%s"] * len(users))

insert_users2 = f"INSERT INTO users (name, age, gender, nationality) VALUES {user_records}"

# execute_query(connection=connection, query=insert_users2, values=users)

select_all_users = "SELECT * FROM users;"
# users = execute_read_query(connection, select_all_users)
# if users:
#     for user in users:
#         print(user)
# else:
#     print('no any users')

select_users_posts = """
SELECT 
    users.id, users.name, posts.description, posts.title
FROM
    posts
    INNER JOIN users ON users.id = posts.user_id
WHERE
    users.age >= 30
;"""

# posts = execute_read_query(connection, select_users_posts)

# for user_post in posts:
#     print(user_post)


select_posts_comments_users = """
SELECT 
    users.id as user_id,
    users.name as name,
    posts.id as post_id,
    posts.description as desc,
    comments.text as comment
FROM
    posts
    INNER JOIN comments ON posts.id = comments.post_id
    INNER JOIN users ON users.id = comments.user_id
;"""

# posts = execute_read_query(connection, select_posts_comments_users)

# for user_post in posts:
#     print(user_post)

select_post_like = """
SELECT
    description as post,
    COUNT(likes.id) as likes
FROM
    likes,
    posts
WHERE
    posts.id = likes.post_id
GROUP BY
    post
;"""

# posts = execute_read_query(connection, select_post_like)
#
# for user_post in posts:
#     print(user_post)

update_post_desc = """
UPDATE
    posts
SET
    description = 'yechize jadid',
    title = 'title jadid'
WHERE
    id = 3
;"""

# execute_query(connection, update_post_desc)

delete_comment = "DELETE FROM comments WHERE id = 4"

execute_query(connection, delete_comment)

