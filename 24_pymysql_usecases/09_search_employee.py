"""
Example 09: Search Employee by Name

Concept:
This example searches employees using LIKE operator.
"""

import pymysql
from db_config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

search_text = "ra"

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

    search_query = """
    SELECT * FROM employees
    WHERE first_name LIKE %s OR last_name LIKE %s
    """

    search_pattern = f"%{search_text}%"
    cursor.execute(search_query, (search_pattern, search_pattern))

    employees = cursor.fetchall()

    print(f"Search results for '{search_text}':")
    print("-" * 80)

    for employee in employees:
        print(employee)

except pymysql.MySQLError as error:
    print("Search operation failed:", error)

finally:
    if "connection" in locals() and connection.open:
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
