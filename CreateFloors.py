import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *




clr.AddReference("RevitServices")
import RevitServices 
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

doc = DocumentManager.Instance.CurrentDBDocument


ArrayCurves = IN[0]
floorType = UnwrapElement(IN[1])
levels = UnwrapElement(IN[2])
structural = IN[3]

curveList = []
out = []

builtInParam = BuiltInParameter.FLOOR_HEIGHTABOVELEVEL_PARAM

for curve in ArrayCurves:
    curveArray = CurveArray()
    for c in curve:
        curveArray.Append(c.ToRevitType())
    curveList.Add(curveArray)

for l in levels:
    for c in curveList:
        TransactionManager.Instance.EnsureInTransaction(doc)
        newFloor = doc.Create.NewFloor(c, floorType, l, structural)
        p = newFloor.get_Parameter(builtInParam)
        p.Set(0)
        out.Add(newFloor.ToDSType(False))
        TransactionManager.Instance.TransactionTaskDone()

OUT = out