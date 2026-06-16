"""
Example 08: Delete Employee

Concept:
This example deletes an employee based on emp_id.
"""

import pymysql
from db_config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

emp_id = 106

try:
    connection = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    cursor = connection.cursor()

    delete_query = "DELETE FROM employees WHERE emp_id = %s"
    cursor.execute(delete_query, (emp_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print(f"Employee {emp_id} deleted successfully.")
    else:
        print(f"No employee found with emp_id {emp_id}.")

except pymysql.MySQLError as error:
    print("Delete operation failed:", error)

finally:
    if "connection" in locals() and connection.open:
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
