"""
Example 05: Select All Employees

Concept:
This example fetches all records from the employees table.
"""

import pymysql
from db_config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

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

    select_query = "SELECT * FROM employees"
    cursor.execute(select_query)

    employees = cursor.fetchall()

    print("Employee Records:")
    print("-" * 80)

    for employee in employees:
        print(
            employee["emp_id"],
            employee["first_name"],
            employee["last_name"],
            employee["email"],
            employee["department"],
            employee["salary"]
        )

except pymysql.MySQLError as error:
    print("Select operation failed:", error)

finally:
    if "connection" in locals() and connection.open:
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
