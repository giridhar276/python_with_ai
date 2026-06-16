"""
Example 01: Create MySQL Database

Concept:
This example connects to MySQL server and creates a database.

Before running:
1. Make sure MySQL server is running.
2. Update .env file with correct username and password.
"""

import pymysql
from db_config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

try:
    connection = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD
    )

    cursor = connection.cursor()

    query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"
    cursor.execute(query)

    print(f"Database '{DB_NAME}' created successfully or already exists.")

except pymysql.MySQLError as error:
    print("Database creation failed:", error)

finally:
    if "connection" in locals() and connection.open:
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
