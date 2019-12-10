"""
ModifyRotateElements
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
Sample on how to rotate model elements.
Use this sample along with the Video on Youtube.
""" 
import clr
# import Revit Servies 
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# import Revit Nodes 
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
# import Revit API
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
# import system
clr.AddReference("System")
from System.Collections.Generic import *
# get current Revit document. 
doc = DocumentManager.Instance.CurrentDBDocument
# Dynamo inputs
elements = UnwrapElement(IN[0])
angle = IN[1]
# loop over each element
for e in elements:
    # reference point to pivot 
    ref_location = e.Location.Point
    # line to pivot around. 
    rot_axis = Line.CreateBound(ref_location, XYZ(ref_location.X, ref_location.Y,ref_location.Z+1.0))
    # start Revit transcation 
    TransactionManager.Instance.EnsureInTransaction(doc)
    # rotate elements 
    ElementTransformUtils.RotateElement(doc, e.Id, rot_axis, angle)
    # end Revit transaction 
    TransactionManager.Instance.TransactionTaskDone()