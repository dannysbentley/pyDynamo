import clr

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def CheckParameter(parameter):
	storageType = parameter.StorageType
	if(storageType.ToString() == "ElementId"):
		value = parameter.AsValueString()
		
	return value
	
doc = DocumentManager.Instance.CurrentDBDocument

elem = UnwrapElement(IN[0])
out = []

for e in elem:
	p = []
	id = e.Id
	name = e.Name
	workset = doc.GetWorksetTable().GetWorkset(e.WorksetId).Name
	length = e.get_Parameter(BuiltInParameter.CURVE_ELEM_LENGTH).AsValueString()
	volume = e.get_Parameter(BuiltInParameter.HOST_VOLUME_COMPUTED).AsDouble()
	baseLevel = e.get_Parameter(BuiltInParameter.WALL_BASE_CONSTRAINT)
	value = CheckParameter(baseLevel)
	
	p.append(id)
	p.append(name)
	p.append(workset)
	p.append(length)
	p.append(volume)
	p.append(value)
	
	out.append(p)
	
OUT = out