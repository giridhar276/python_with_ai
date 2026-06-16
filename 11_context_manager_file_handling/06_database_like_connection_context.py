# Topic: Context Manager
# Example: Database-like connection

class DatabaseConnection:
    def __enter__(self):
        print("Database connected")
        return self

    def query(self, sql):
        print("Executing query:", sql)

    def __exit__(self, exc_type, exc_value, traceback):
        print("Database connection closed")

with DatabaseConnection() as db:
    db.query("SELECT * FROM employees")
