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


outList = []
familyType = []

for i in UnwrapElement(elements):
    p = i.LookupParameter("APZ Status")
    TransactionManager.Instance.EnsureInTransaction(doc)
    p.Set("Setting a Parameter")
    TransactionManager.Instance.TransactionTaskDone()

