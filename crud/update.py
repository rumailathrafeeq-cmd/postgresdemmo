import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import get_db_connection

def table_update(id,new_name):
    conn=get_db_connection()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query='''
            UPDATE users 
            SET name=%s
            WHERE id=%s;
            '''

            cursor.execute(query,(id,new_name))
            conn.commit()
            print('user updated successfully')
        except Exception as e:
            print(f'An error occured:{e}')
        finally:
            cursor.close()
            conn.close()
table_update('zeba',2)