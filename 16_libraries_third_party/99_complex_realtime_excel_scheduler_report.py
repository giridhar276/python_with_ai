# Topic: Complex Third-party Libraries
# Example: Scheduled Excel report

import os
from datetime import datetime

try:
    from openpyxl import Workbook
except ImportError:
    print("Please install openpyxl: pip install openpyxl")
    raise SystemExit

try:
    import schedule
except ImportError:
    print("Please install schedule: pip install schedule")
    raise SystemExit

def generate_excel_report():
    output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "scheduled_report.xlsx")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Report"
    sheet.append(["Generated At", "Status"])
    sheet.append([datetime.now().isoformat(), "Success"])
    workbook.save(output_file)

    print("Report generated:", output_file)

schedule.every(1).seconds.do(generate_excel_report)

for _ in range(2):
    schedule.run_pending()

    import time
    time.sleep(1)
