"""
Example 11: Drop Table - Optional

Warning:
Run this only when you want to delete the employees table completely.
"""

import pymysql
from db_config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

confirm = input("Type YES to drop employees table: ")

if confirm != "YES":
    print("Operation cancelled.")
else:
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        cursor = connection.cursor()

        drop_query = "DROP TABLE IF EXISTS employees"
        cursor.execute(drop_query)

        print("Employees table dropped successfully.")

    except pymysql.MySQLError as error:
        print("Drop table operation failed:", error)

    finally:
        if "connection" in locals() and connection.open:
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
