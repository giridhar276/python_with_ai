"""
Example 07: Update Employee Salary

Concept:
This example updates salary for a given employee ID.
"""

import pymysql
from db_config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

emp_id = 101
new_salary = 60000

try:
    connection = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    cursor = connection.cursor()

    update_query = "UPDATE employees SET salary = %s WHERE emp_id = %s"
    cursor.execute(update_query, (new_salary, emp_id))
    connection.commit()

    if cursor.rowcount > 0:
        print(f"Employee {emp_id} salary updated successfully.")
    else:
        print(f"No employee found with emp_id {emp_id}.")

except pymysql.MySQLError as error:
    print("Update operation failed:", error)

finally:
    if "connection" in locals() and connection.open:
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
