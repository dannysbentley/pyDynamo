import clr

clr.AddReference('Microsoft.Office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel
from System import Array

path = IN[0]

# Instantiate the Excel Application
ex = Excel.ApplicationClass()
# Make it Visiable for us all to see
ex.Visible = True
# Disable Alerts - Errors Ignore them, they're probably not important
ex.DisplayAlerts = False
# Workbook
workbook = ex.Workbooks.Open(path)
# WorkSheet
ws = workbook.Worksheets[1]
i = 0
# Cell range
x1range = ws.Range["A1", "A4"]
sheetName = IN[1]
a = Array.CreateInstance(object, len(sheetName),1) # row and column

while i < len(sheetName):
    a[i,0] = sheetName[i]
    i += 1

x1range.Value2 = a