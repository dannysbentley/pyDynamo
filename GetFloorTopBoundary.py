"""
GetFloorTopBoundary
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__version__ = '1.0.0'

"""
Sample on how to get the analytical surface of a floor.
Use this sample along with the Video on Youtube.
"""
import clr
# import Revit API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB.Structure import *
# import Revit Services
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# Get the current Revit document. 
doc = DocumentManager.Instance.CurrentDBDocument

#Functions for list handling
def ProcessList(_func, _list):
    return map( lambda x: ProcessList(_func, x) if type(x)==list else _func(x), _list )

#Preparing input from dynamo to revit
if isinstance(IN[0], list):
	analyticalFloor = ProcessList(UnwrapElement, IN[0])
else:
	analyticalFloor = []
	analyticalFloor.append(UnwrapElement(IN[0]))

#Create a dictionary for getting the correct enum
prjOptEnum = { 
"Top of Element" : SurfaceElementProjectionZ.TopOrInterior, 
"Bottom of Element" : SurfaceElementProjectionZ.BottomOrExterior,
"Center of Element" : SurfaceElementProjectionZ.CenterOfElement,
}
#Look uo the the enum
projOption = prjOptEnum[IN[1]]

#Define function for API method:
def setProjection(aFloor,pOption = projOption):
		aFloor.ProjectionZ=pOption

#Change projection method in a transaction
TransactionManager.Instance.EnsureInTransaction(doc)

ProcessList(setProjection,analyticalFloor)

TransactionManager.Instance.TransactionTaskDone()

OUT = analyticalFloor

