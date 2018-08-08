"""
ModifyRotateView
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__version__ = '1.0.0'

"""
Sample on how to rotate section view.
Use this sample along with the Video on Youtube.
""" 
import clr
import math
# import Revit API
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *
# import Revit Services 
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# get the current Revit document
doc = DocumentManager.Instance.CurrentDBDocument
#selected element 
# Dynamo input 
section = UnwrapElement(IN[0])
angle = math.radians(IN[1])
view = UnwrapElement(IN[2])
# start transaction in Revit.
TransactionManager.Instance.EnsureInTransaction(doc)
# get bounding box of view 
bbox = section.BoundingBox[view]
# create a line from the bouding box 
diag = Line.CreateBound(bbox.Min, bbox.Max)
# make point 1
p1 = diag.Evaluate(0.5, True)
# make point 2
p2 = XYZ(p1.X, p1.Y, p1.Z+1)
# make line using the two points. 
axis_ = Line.CreateBound(p1,p2)
# rotate model elements. 
Autodesk.Revit.DB.ElementTransformUtils.RotateElement(doc, section.Id, axis_, angle)
# end transaction in Revit. 
TransactionManager.Instance.TransactionTaskDone()

OUT = section