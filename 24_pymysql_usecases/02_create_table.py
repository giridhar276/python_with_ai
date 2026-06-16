"""
Example 02: Create Employees Table

Concept:
This example creates an employees table with 6 columns.

Columns:
emp_id, first_name, last_name, email, department, salary
"""

import pymysql
from db_config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

try:
    connection = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INT PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        department VARCHAR(50),
        salary DECIMAL(10, 2)
    )
    """

    cursor.execute(create_table_query)
    print("Employees table created successfully or already exists.")

except pymysql.MySQLError as error:
    print("Table creation failed:", error)

finally:
    if "connection" in locals() and connection.open:
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
