"""
CreateFloors
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__version__ = '1.0.0'

"""
Sample on how to create multiple floors.
Use this sample along with the Video on Youtube.
"""
import clr
# import ProtoGeometry
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
# import Revit API
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
# import RevitServices
clr.AddReference("RevitServices")
import RevitServices 
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# import RevitNodes
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
# get current Revit document. 
doc = DocumentManager.Instance.CurrentDBDocument
# Dynamo input 
ArrayCurves = IN[0] # array curves to build slab
floorType = UnwrapElement(IN[1]) # Floor Type to apply
levels = UnwrapElement(IN[2]) # levels to create floor. 
structural = IN[3] # is floor structural. 
# Empty list 
curveList = []
out = []
# built in paramter of floor offset. 
builtInParam = BuiltInParameter.FLOOR_HEIGHTABOVELEVEL_PARAM
# loop over curves to add to list. 
for curve in ArrayCurves:
    curveArray = CurveArray()
    for c in curve:
        curveArray.Append(c.ToRevitType())
    curveList.Add(curveArray)
# loop over each floor and curve list to build floor on each level.
for l in levels:
    for c in curveList:
		# start Revit transaction. 
        TransactionManager.Instance.EnsureInTransaction(doc)
		# create new floor in Revit. 
        newFloor = doc.Create.NewFloor(c, floorType, l, structural)
		# set offset of floor from level. 
        p = newFloor.get_Parameter(builtInParam)
        p.Set(0)
		# convert to Dynamo element to send out. 
        out.Add(newFloor.ToDSType(False))
        TransactionManager.Instance.TransactionTaskDone()

OUT = out