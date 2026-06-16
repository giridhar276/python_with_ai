"""
Example 03: Insert Single Employee

Concept:
This example inserts one employee record into the employees table.

Important:
Use parameterized queries to avoid SQL injection.
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

    insert_query = """
    INSERT INTO employees
    (emp_id, first_name, last_name, email, department, salary)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    employee_data = (
        100,
        "Arjun",
        "Verma",
        "arjun.verma@example.com",
        "Admin",
        50000
    )

    cursor.execute(insert_query, employee_data)
    connection.commit()

    print("Single employee inserted successfully.")

except pymysql.err.IntegrityError as error:
    print("Duplicate or constraint error:", error)

except pymysql.MySQLError as error:
    print("Insert operation failed:", error)

finally:
    if "connection" in locals() and connection.open:
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
