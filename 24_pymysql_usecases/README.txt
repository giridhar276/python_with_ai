# Simple Python PyMySQL Employee Examples

This folder contains beginner-friendly PyMySQL examples using an `employees.csv` file.

All files are kept in the same folder for easy classroom execution.

## Folder Structure

```text
pymysql_employee_examples_single_folder/
│
├── employees.csv
├── requirements.txt
├── .env.example
├── README.txt
├── TRAINER_NOTES.txt
├── db_config.py
├── 01_create_database.py
├── 02_create_table.py
├── 03_insert_single_employee.py
├── 04_insert_from_csv.py
├── 05_select_all_employees.py
├── 06_select_with_condition.py
├── 07_update_employee.py
├── 08_delete_employee.py
├── 09_search_employee.py
├── 10_transaction_example.py
└── 11_drop_table_optional.py
```

## Step 1: Install MySQL

Install MySQL Server on your system.

For Mac:

```bash
brew install mysql
brew services start mysql
```

For Ubuntu/Linux:

```bash
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
```

For Windows:

Install MySQL Server using the MySQL Installer.

## Step 2: Install Python Packages

Open terminal inside this folder and run:

```bash
pip install -r requirements.txt
```

## Step 3: Create `.env` File

Copy `.env.example` and rename it as `.env`.

Update your MySQL username and password:

```text
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=employee_db
```

## Step 4: Run Examples in Order

Run these files one by one from the same folder:

```bash
python 01_create_database.py
python 02_create_table.py
python 03_insert_single_employee.py
python 04_insert_from_csv.py
python 05_select_all_employees.py
python 06_select_with_condition.py
python 07_update_employee.py
python 08_delete_employee.py
python 09_search_employee.py
python 10_transaction_example.py
```

## Operations Covered

- Connect to MySQL
- Create database
- Create table
- Insert one employee
- Insert employees from CSV
- Select all employees
- Select employees with condition
- Update employee
- Delete employee
- Search employee
- Transaction with commit and rollback
- Optional drop table example

## Important Notes

1. Run `01_create_database.py` first.
2. Run `02_create_table.py` second.
3. Run `04_insert_from_csv.py` before select/update/delete examples.
4. Use parameterized queries to avoid SQL injection.
5. Use `commit()` for INSERT, UPDATE, and DELETE.
6. Use `rollback()` for transaction failure.
