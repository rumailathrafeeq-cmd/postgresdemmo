import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import get_db_connection

from db import get_db_connection

def check_user(name):
    conn = get_db_connection()

    if conn is not None:
        try:
            cursor = conn.cursor()

            query = """
            SELECT * FROM users
            WHERE name = %s;
            """

            cursor.execute(query, (name,))
            user = cursor.fetchone()

            if user:
                print(f"User found: {user}")
            else:
                print("User not found")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            cursor.close()
            conn.close()
# check_user('zeba')