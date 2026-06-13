import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import get_db_connection

def delete_user(id):
    conn = get_db_connection()

    if conn is not None:
        try:
            cursor = conn.cursor()

            query = """
            DELETE FROM users
            WHERE id = %s;
            """

            cursor.execute(query, (id,))
            conn.commit()

            print("User deleted successfully")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            cursor.close()
            conn.close()
# delete_user(2)