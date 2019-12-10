"""
ApplyViewTemplate
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
Sample on how to apply a view template.
Use this sample along with the Video on Youtube.
"""
import clr
# Import Revit Services to access document and transaction.
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# Import RevitAPI 
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
# Get the current Revit Document. 
doc = DocumentManager.Instance.CurrentDBDocument
# Input 
viewTempName = IN[1]
# Empty list of views. 
views = []
# loop over input. 
for i in IN[0]:
	views.append(UnwrapElement(i))
# start Revit transaction. 
TransactionManager.Instance.EnsureInTransaction(doc)
# collect all the views in project
collector = FilteredElementCollector(doc).OfClass(View)
# loop over views and check view is view template and view name.
for i in collector:
    if i.IsTemplate == True and i.Name == viewTempName:
        viewTemp = i
# for each view from input apply view template with id. 
for i in views:
    i.ViewTemplateId = viewTemp.Id
# close transaction
TransactionManager.Instance.TransactionTaskDone()

OUT = views