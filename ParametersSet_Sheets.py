import clr
import sys

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager 

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

doc = DocumentManager.Instance.CurrentDBDocument
app = DocumentManager.Instance.CurrentUIApplication.Application

uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

elements = IN[0]


for i in UnwrapElement(elements):
	#Get All Parameters
    SheetIssueDate = i.LookupParameter("Sheet Issue Date")
    CheckedBy = i.LookupParameter("Checked By")
    DrawnBy = i.LookupParameter("Drawn By")
    
    TransactionManager.Instance.EnsureInTransaction(doc)
    #Set Parameters
    SheetIssueDate.Set(" ")
    CheckedBy.Set("LEAD")
    DrawnBy.Set("TEAM")
    TransactionManager.Instance.TransactionTaskDone()
    

OUT = 0