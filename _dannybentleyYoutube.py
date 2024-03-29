#Copyright(c) 2016, Dimitar Venkov
# @5devene, dimitar.ven@gmail.com

import clr

clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

def tolist(obj1):
	if hasattr(obj1,"__iter__"): return obj1
	else: return [obj1]

sheets = UnwrapElement(tolist(IN[0]))
sheet_hasNoViews = []
rev_str = "<Revision Schedule>"
sched_dict = dict()
fec1 = FilteredElementCollector(doc).OfClass(ScheduleSheetInstance)

for s in fec1:
	if rev_str not in s.Name:
		key = s.OwnerViewId.IntegerValue
		if key not in sched_dict:
			sched_dict[key] = [s]
		else:
			sched_dict[key].append(s)

for i in xrange(len(sheets) ):
	viewsid = sheets[i].GetAllPlacedViews()
	if viewsid.count > 0:
        sheet_hasNoViews.append(sheet[i])
OUT = sheet_hasNoViews