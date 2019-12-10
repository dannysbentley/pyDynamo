"""
ParameterSet
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
Sample on how to set a parameter.
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
# import ProtoGeometry 
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
# get Revit's current Document file.
doc = DocumentManager.Instance.CurrentDBDocument
# get the current application 
app = DocumentManager.Instance.CurrentUIApplication.Application
#get the user interface application 
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
# Dynamo input
elements = IN[0]
# Empty list
outList = []
familyType = []
# loop over elements 
for i in UnwrapElement(elements):
    # look up parameter
    p = i.LookupParameter("APZ Status")
    # start Revit transaction
    TransactionManager.Instance.EnsureInTransaction(doc)
    # set parameter. 
    p.Set("Setting a Parameter")
    # end Revit transaction 
    TransactionManager.Instance.TransactionTaskDone()

