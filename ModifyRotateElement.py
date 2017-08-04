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
angle = IN[1]

for e in elements:
    ref_location = e.Location.Point
    rot_axis = Line.CreateBound(ref_location, XYZ(ref_location.X, ref_location.Y,ref_location.Z+1.0))

    TransactionManager.Instance.EnsureInTransaction(doc)
    ElementTransformUtils.RotateElement(doc, e.Id, rot_axis, angle)
    TransactionManager.Instance.TransactionTaskDone()