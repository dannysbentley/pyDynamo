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

doc = DocumentManager.Instance.CurrentDBDocument

def ConvertColor(element):
	return Autodesk.Revit.DB.Color(element.Red, element.Green, element.Blue)

def OverrideElement(element, color, fill):
	ogs = OverrideGraphicSettings()
	ogs.SetProjectionFillColor(color)
	ogs.SetProjectionFillPatternId(fill.Id)
	ogs.SetCutFillColor(color)
	ogs.SetCutFillPatternId(fill.Id)
	doc.ActiveView.SetElementOverrides(element.Id, ogs)

elements = UnwrapElement(IN[0])
colors = ConvertColor(IN[1])
fillPat = UnwrapElement(IN[2])

for i in elements:
    TransactionManager.Instance.EnsureInTransaction(doc)
    OverrideElement(i, colors, fillPat)
    TransactionManager.Instance.TransactionTaskDone()