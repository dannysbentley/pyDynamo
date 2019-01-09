import clr
# Import Revit API
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
# Import Revit Services 
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

floors = UnwrapElement(IN[0])

def getLevel(id):
	for l in UnwrapElement(IN[1]): 
		if(id == l.Id):
			return l

BottomElevParam = BuiltInParameter.STRUCTURAL_ELEVATION_AT_BOTTOM
LevelParam = BuiltInParameter.LEVEL_PARAM

object = []
List = []

for f in floors:
	feet = f.get_Parameter(BottomElevParam).AsDouble()
	meter = feet * 3.281
	id = f.get_Parameter(LevelParam).AsElementId()
	level = getLevel(id)
	object.append(level)
	object.append(meter)
	
List.append(object)	
	
OUT = List