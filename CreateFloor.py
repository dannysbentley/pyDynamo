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

curveArray = CurveArray()

for c in ArrayCurves:
    curveArray.Append(c.ToRevitType())

TransactionManager.Instance.EnsureInTransaction(doc)
newFloor = doc.Create.NewFloor(curveArray, floorType, levels, structural)
out = newFloor.ToDSType(False)
TransactionManager.Instance.TransactionTaskDone()

OUT = out