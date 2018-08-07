"""
RevitLookUpWall
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__version__ = '1.0.0'

"""
Sample on how to use the RevitLookUp Add-in
Use this sample along with the Video on Youtube.
"""
import clr
# Import Revit API
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
# Import services for transactions and document.
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# Check Parameter storage type to get a string value. 
def CheckParameter(parameter):
	storageType = parameter.StorageType
	if(storageType.ToString() == "ElementId"):
		value = parameter.AsValueString()
		
	return value
	
# Get the current document in Revit. 
doc = DocumentManager.Instance.CurrentDBDocument

# The input ports
elem = UnwrapElement(IN[0])
# Empty list to add parameters for each element. 
out = []
# Loop over each element. 
for e in elem:
	#Empty list to add element parameters
	p = []
	# Element id and name
	id = e.Id
	name = e.Name
	# Document workset table to get workset by workset id. 
	workset = doc.GetWorksetTable().GetWorkset(e.WorksetId).Name
	# Built in parameters and value
	length = e.get_Parameter(BuiltInParameter.CURVE_ELEM_LENGTH).AsValueString()
	volume = e.get_Parameter(BuiltInParameter.HOST_VOLUME_COMPUTED).AsDouble()
	# Get base level parameter and use definition to check storage type.
	baseLevel = e.get_Parameter(BuiltInParameter.WALL_BASE_CONSTRAINT)
	value = CheckParameter(baseLevel)
	# add parameter values to list.
	p.append(id)
	p.append(name)
	p.append(workset)
	p.append(length)
	p.append(volume)
	p.append(value)
	# add to out.
	out.append(p)
	
OUT = out