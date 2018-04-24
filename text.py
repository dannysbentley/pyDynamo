import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

def OverrideElement(element, fill):
	ogs = OverrideGraphicSettings()
	ogs.SetProjectionLinePatternId(fill.Id)
	doc.ActiveView.SetElementOverrides(element.Id, ogs)

doc = DocumentManager.Instance.CurrentDBDocument

patterns = FilteredElementCollector(doc).OfClass(LinePatternElement).ToElements()

fillPatSelected = list()

for i in range(len(patterns)):
    namepick = patterns[i].ToDSType(True)
    if namepick.Name == "Hidden":
        fillPatSelected.append(patterns[i])

elements = UnwrapElement(IN[0])


for i in elements:
    TransactionManager.Instance.EnsureInTransaction(doc)
    OverrideElement(i, fillPatSelected[0])
    TransactionManager.Instance.TransactionTaskDone()
    
OUT = elements﻿
    