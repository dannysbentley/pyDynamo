"""
ParameterSet_Sheets
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__version__ = '1.0.0'

"""
Sample on how to set sheet parameters.
Use this sample along with the Video on Youtube.
"""
import clr
import sys
# import Revit API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
# import Revit API UI
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
# import Revit Services
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager 
# import proto geometry 
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
# get the current Revit document
doc = DocumentManager.Instance.CurrentDBDocument
# get the current application 
app = DocumentManager.Instance.CurrentUIApplication.Application
# get the current UI application 
uiapp = DocumentManager.Instance.CurrentUIApplication
# get the appliction. 
app = uiapp.Application
# Dynamo input 
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