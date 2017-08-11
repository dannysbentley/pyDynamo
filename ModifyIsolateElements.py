import clr

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

import System
from System.Collections.Generic import *

doc = DocumentManager.Instance.CurrentDBDocument
ActiveViewElements = FilteredElementCollector(doc, doc.ActiveView.Id).OfClass(Wall).ToElements()
elements = UnwrapElement(ActiveViewElements)
view = UnwrapElement(doc.ActiveView)

ids = list()

for items in elements:
    ids.append(items.Id)

idElements = List[ElementId](ids)

TransactionManager.Instance.EnsureInTransaction(doc)
view.IsolateElementsTemporary(idElements)
TransactionManager.Instance.TransactionTaskDone()