import clr

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import XYZ, Line, Wall

length = IN[0]
level = UnwrapElement(IN[1])

pt1 = XYZ(0, 0, 0)
pt2 = XYZ(length, 0, 0)


TransactionManager.Instance.EnsureInTransaction(doc)

line = Line.CreateBound(pt1, pt2)
wall = Wall.Create(doc, line, level.Id, False)

TransactionManager.Instance.TransactionTaskDone()	

OUT = wall