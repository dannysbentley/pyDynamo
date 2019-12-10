"""
CreateFloor
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
Sample on how to create a floor.
Use this sample along with the Video on Youtube.
"""
import clr
#import ProtoGeometry
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
#import Revit API
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
# Get the current document from Revit.
doc = DocumentManager.Instance.CurrentDBDocument
# Input from Dynamo. 
ArrayCurves = IN[0] # Array of curves 
floorType = UnwrapElement(IN[1]) # Floor Type 
levels = UnwrapElement(IN[2]) # levels 
structural = IN[3] # Structural usage
# create an empty list. 
curveArray = CurveArray()
# loop over input of array curves 
for c in ArrayCurves:
    curveArray.Append(c.ToRevitType())

# Start Revit transaction 
TransactionManager.Instance.EnsureInTransaction(doc)
# Create new floor in Revit. 
newFloor = doc.Create.NewFloor(curveArray, floorType, levels, structural)
# Convert to Dynamo gemoetry to send out to Dynamo. 
out = newFloor.ToDSType(False)
# Complete transaction in Revit. 
TransactionManager.Instance.TransactionTaskDone()

OUT = out