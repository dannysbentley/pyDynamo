"""
ModifyDimensionText
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__version__ = '1.0.0'

"""
Sample on how to override dimension text.
Use this sample along with the Video on Youtube.
""" 
import clr
# import Revit API
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
# import Revit Services 
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# get current Revit document. 
doc = DocumentManager.Instance.CurrentDBDocument
# Dynamo input 
dimensions = UnwrapElement(IN[0])
# transaction start in Revit
TransactionManager.Instance.EnsureInTransaction(doc)
# empty list
MyList = []
# loop over dimensions and override. 
for i in dimensions:
    i.ValueOverride = "."
    MyList.append(i.ValueOverride)
# Finish Revit transaction. 
TransactionManager.Instance.TransactionTaskDone()

OUT = MyList