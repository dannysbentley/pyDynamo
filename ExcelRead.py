"""
ExcelRead
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
Sample on how to read an excel file.
Use this sample along with the Video on Youtube.
"""
import clr
# import the Excel Interop. 
clr.AddReference('Microsoft.Office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel
from System.Runtime.InteropServices import Marshal
# file path of excel file. 
path = IN[0]

# Instantiate the Excel Application
ex = Excel.ApplicationClass()
# Make it Visiable for us all to see
ex.Visible = False
# Disable Alerts - Errors Ignore them, they're probably not important
ex.DisplayAlerts = False
# Workbook 
workbook = ex.Workbooks.Open(path)
# WorkSheet
ws = workbook.Worksheets[1]
# Cell range
x1range = ws.Range["A1", "A4"]
x2range = ws.Range["B1", "B4"]
 
r1 = x1range.Value2
r2 = x2range.Value2

OUT = r1, r2
# close and release excel file from memory. 
ex.ActiveWorkbook.Close(False)
Marshal.ReleaseComObject(ws)
Marshal.ReleaseComObject(workbook)
Marshal.ReleaseComObject(ex)