import clr

clr.AddReference('Microsoft.Office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel
from System.Runtime.InteropServices import Marshal

path = IN[0]
ex = Excel.ApplicationClass()
ex.Visible = False
ex.DisplayAlerts = False

workbook = ex.Workbooks.Open(path)
ws = workbook.Worksheets[1]
x1range = ws.Range["A1", "A4"]
x2range = ws.Range["B1", "B4"]

r1 = x1range.Value2
r2 = x2range.Value2

OUT = r1, r2

ex.ActiveWorkbook.Close(False)
Marshal.ReleaseComObject(ws)
Marshal.ReleaseComObject(workbook)
Marshal.ReleaseComObject(ex)