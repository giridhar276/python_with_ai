"""
Example 06: Select Employees with Condition

Concept:
This example fetches employees from a specific department.
"""

import pymysql
from db_config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

department_name = "IT"

try:
    connection = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

    cursor = connection.cursor()

    select_query = "SELECT * FROM employees WHERE department = %s"
    cursor.execute(select_query, (department_name,))

    employees = cursor.fetchall()

    print(f"Employees from {department_name} department:")
    print("-" * 80)

    for employee in employees:
        print(employee)

except pymysql.MySQLError as error:
    print("Conditional select failed:", error)

finally:
    if "connection" in locals() and connection.open:
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
