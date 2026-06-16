"""
Example 10: Transaction Example

Concept:
A transaction groups multiple SQL operations.
If one operation fails, rollback will cancel all changes.

Scenario:
1. Insert one employee.
2. Update salary of another employee.
3. Commit both changes together.
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
    ON DUPLICATE KEY UPDATE
        salary = VALUES(salary)
    """

    update_query = "UPDATE employees SET salary = salary + 5000 WHERE emp_id = %s"

    cursor.execute(
        insert_query,
        (107, "Kiran", "Das", "kiran.das@example.com", "Support", 47000)
    )

    cursor.execute(update_query, (102,))

    connection.commit()
    print("Transaction completed successfully.")

except pymysql.MySQLError as error:
    if "connection" in locals() and connection.open:
        connection.rollback()
    print("Transaction failed. Rollback completed.")
    print("Error:", error)

finally:
    if "connection" in locals() and connection.open:
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
