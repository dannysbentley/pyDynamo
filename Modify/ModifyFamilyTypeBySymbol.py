import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

familyInstance = UnwrapElement(IN[0])
familyType = UnwrapElement(IN[1])
count = 0
TransactionManager.Instance.EnsureInTransaction(doc)
for item in familyInstance:
    item.Symbol = familyType
    count += 1
TransactionManager.Instance.TransactionTaskDone()