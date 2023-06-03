import openpyxl
from openpyxl.styles import Font

wb = openpyxl.load_workbook('./test.xlsx', data_only=True)
ws = wb["Sheet1"]

cells = ws['B':'B']

new_font = Font(size=20, bold=True)

white_list = ['김부자', '박평범']

for cell in cells:
    try:
        name = cell.value
        if name in white_list:
            cell.font = new_font
    except: 
        pass

wb.save('test_result.xlsx')