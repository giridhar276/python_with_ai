# Topic: OOP Concepts
# Example: 11 polymorphism

class PDFReport:
    def generate(self):
        print('Generating PDF report')

class ExcelReport:
    def generate(self):
        print('Generating Excel report')

for report in [PDFReport(), ExcelReport()]:
    report.generate()
