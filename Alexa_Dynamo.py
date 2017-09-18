import clr
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

import System
from System.Collections.Generic import *

dataEnteringNode = IN

doc = DocumentManager.Instance.CurrentDBDocument
switch = IN[0]

builtInCategory = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_GenericAnnotation).WhereElementIsNotElementType().ToElements()


SFDUG = list(filter(lambda w : w.Name.Equals("HELLO"), builtInCategory))

if switch == 0:
	for i in UnwrapElement(SFDUG):
		p= i.LookupParameter("SFDUG")
		TransactionManager.Instance.EnsureInTransaction(doc)
		p.Set("Hello SFDUG")
		TransactionManager.Instance.TransactionTaskDone()

if switch == 1:
	for i in UnwrapElement(SFDUG):
		p= i.LookupParameter("SFDUG")
		TransactionManager.Instance.EnsureInTransaction(doc)
		p.Set("")
		TransactionManager.Instance.TransactionTaskDone()

OUT = "done"