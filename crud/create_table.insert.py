import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import get_db_connection

def table_insert(name):
    conn=get_db_connection()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query='''
            INSERT INTO users (name)
            VALUES(%s);
            '''

            cursor.execute(query,(name,))
            conn.commit()
            print('Users inserted successfully')
        except Exception as e:
            print(f'An error occures:{e}')
        finally:
            cursor.close()
            conn.close
table_insert('Rumailath')


