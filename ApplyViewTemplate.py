import clr

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

viewTempName = IN[1]
views = []
for i in IN[0]:
	views.append(UnwrapElement(i))

TransactionManager.Instance.EnsureInTransaction(doc)

collector = FilteredElementCollector(doc).OfClass(View)
for i in collector:
	if i.IsTemplate == True and i.Name == viewTempName:
		viewTemp = i

for i in views:
	i.ViewTemplateId = viewTemp.Id
		
TransactionManager.Instance.TransactionTaskDone()

OUT=views