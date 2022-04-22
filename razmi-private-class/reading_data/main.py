import pandas as pd
import psycopg2
from psycopg2 import OperationalError
from sqlalchemy import create_engine
import openpyxl
import xlrd
import datetime

conn_string = 'postgresql://postgres:1234qwer@localhost/razmi'

db = create_engine(conn_string)
conn = db.connect()

# df = pd.read_csv('Book1.csv')
# df.to_sql('data', con=conn, if_exists='replace', index=True)
# df.to_sql('data', con=conn, if_exists='append', index=True)

# latolong_data = pd.read_excel('LAT-LONG.xlsx')
# latolong_data.to_sql('latolong_data', con=conn, if_exists='replace', index=True)


conn = psycopg2.connect(conn_string)
conn.autocommit = True
cursor = conn.cursor()

sql1 = "select * from data;"
cursor.execute(sql1)
all_data = cursor.fetchall()
for item in all_data:
    final_result = {}
    latolong = str(item[2]) + str(item[3])
    final_result['latolong'] = latolong
    cursor2 = conn.cursor()
    cursor2.execute(f" select * from latolong_data where id = '{latolong}';")
    result = cursor2.fetchall()
    if result:
        final_result['base_id'] = result[0][2]
        final_result['region'] = result[0][9]
        str_datetime = str(item[1])
        obj_datetime = datetime.datetime.strptime(str_datetime, "%Y%m%d")
        final_result['week_num'] = f"{obj_datetime.year}-Wk{obj_datetime.strftime('%V')}"
        if item[15] > 100_000_000:
            final_result['valid_invalid'] = 1
        else:
            final_result['valid_invalid'] = 0


# conn.commit()
conn.close()
