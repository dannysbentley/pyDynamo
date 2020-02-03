__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

from System.Collections.Generic import List

# collect current document. 
doc = DocumentManager.Instance.CurrentDBDocument
# collect linked revit documents 
linkedDoc = FilteredElementCollector(doc).OfClass(RevitLinkInstance)
#
linkDoc, transform = [], []

# get the linked document and transform 
for i in linkedDoc:
	linkDoc.append(i.GetLinkDocument())
	transform.append(i.GetTotalTransform())
	
# collect all grids from linked document. 
elements = FilteredElementCollector(linkDoc[0]).OfCategory(BuiltInCategory.OST_Matchline).WhereElementIsNotElementType().ToElements()
# list of elements ids 
ids = List[ElementId]()
# add all elements ids to list 
for i in elements:
	ids.Add(i.Id)

# Copy elements from linked model to current model. 
TransactionManager.Instance.EnsureInTransaction(doc)
copy = ElementTransformUtils.CopyElements(linkDoc[0], ids, doc, transform[0], None)
TransactionManager.Instance.TransactionTaskDone()

OUT = linkDoc[0]