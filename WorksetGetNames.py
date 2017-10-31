import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
elements = UnwrapElement(IN[0])

WorksetIDList = list()
WorksetNameList = list()

for e in elements:
    WorksetIDList.append(doc.GetWorksetTable().GetWorkset(e.WorksetId))

for ws in WorksetIDList:
    WorksetNameList.append(ws.Name)

OUT = WorksetNameList