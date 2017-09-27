import clr

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

dimensions = UnwrapElement(IN[0])

TransactionManager.Instance.EnsureInTransaction(doc)
MyList = []
for i in dimensions:
    i.ValueOverride = "."
    MyList.append(i.ValueOverride)
    
TransactionManager.Instance.TransactionTaskDone()

OUT = MyList