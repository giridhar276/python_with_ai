# Topic: User Defined Functions
# Example: Default arguments

def generate_report(report_name, file_format="pdf"):
    print(f"Generating {report_name}.{file_format}")

generate_report("sales_summary")
generate_report("employee_report", "xlsx")
