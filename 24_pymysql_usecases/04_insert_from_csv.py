"""
Example 04: Insert Employees from CSV File

Concept:
This example reads employees.csv and inserts all records into MySQL.

CSV Columns:
emp_id, first_name, last_name, email, department, salary
"""

import csv
from pathlib import Path
import pymysql
from db_config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

csv_file_path = Path(__file__).resolve().parent / "employees.csv"

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
        first_name = VALUES(first_name),
        last_name = VALUES(last_name),
        email = VALUES(email),
        department = VALUES(department),
        salary = VALUES(salary)
    """

    with open(csv_file_path, mode="r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)

        records = []
        for row in csv_reader:
            records.append((
                int(row["emp_id"]),
                row["first_name"],
                row["last_name"],
                row["email"],
                row["department"],
                float(row["salary"])
            ))

    cursor.executemany(insert_query, records)
    connection.commit()

    print(f"{cursor.rowcount} records inserted or updated from CSV.")

except FileNotFoundError:
    print("employees.csv file not found.")

except pymysql.MySQLError as error:
    print("CSV insert operation failed:", error)

finally:
    if "connection" in locals() and connection.open:
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
