"""
CreateSheet
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__version__ = '1.0.0'

"""
Sample on how to create a Sheet.
Use this sample along with the Video on Youtube.
"""
import clr
# Import RevitNodes
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
# import RevitServices
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# Import Revit API 
import RevitServices
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk
# import System
import System
# get the current Revit Doument. 
doc = DocumentManager.Instance.CurrentDBDocument
# Dynamo inputs 
sheetnames = IN[0] # sheet names 
sheetNumber = IN[1] # sheet numbers
titleblock = UnwrapElement(IN[2]) # titleblock type. 
# empty sheet list. 
sheetlist = list()
# begin Revit transaction. 
TransactionManager.Instance.EnsureInTransaction(doc)
# loop over the sheet number to create sheets. 
for number in range(len(sheetNumber)):
	# Create new sheet. 
    newsheet = ViewSheet.Create(doc, titleblock.Id)
	# apply sheet name
    newsheet.Name = sheetnames[number]
	# apply sheet number 
    newsheet.SheetNumber = sheetNumber[number]
	# add to sheet list to send out to Dynamo
    sheetlist.append(newsheet.ToDSType(False))

# complete transaction in Revit. 
TransactionManager.Instance.TransactionTaskDone()
OUT = sheetlist