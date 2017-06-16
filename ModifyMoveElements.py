import clr

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

clr.AddReference("System")
from System.Collections.Generic import *

elements = UnwrapElement(IN[0])
newLocation = IN[1].ToXyz()

Ids = List[ElementId]()
for e in elements:
    Ids.Add(e.Id)

TransactionManager.Instance.EnsureInTransaction(doc)
ElementTransformUtils.MoveElements(doc, Ids, newLocation)
TransactionManager.Instance.TransactionTaskDone()

OUT = Ids