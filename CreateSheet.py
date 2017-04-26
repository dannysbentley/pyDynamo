import clr
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk
import System

from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
sheetnames = IN[0]
sheetNumber = IN[1]
titleblock = UnwrapElement(IN[2])
sheetlist = list()

TransactionManager.Instance.EnsureInTransaction(doc)

for number in range(len(sheetNumber)):
    newsheet = ViewSheet.Create(doc, titleblock.Id)
    newsheet.Name = sheetnames[number]
    newsheet.SheetNumber = sheetNumber[number]
    sheetlist.append(newsheet.ToDSType(False))

TransactionManager.Instance.TransactionTaskDone()
OUT = sheetlist