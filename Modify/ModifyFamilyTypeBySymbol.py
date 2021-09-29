"""
Change the Element's workset.
"""
__author__ = 'Danny Bentley'
__version__ = '2021.09.29'

import clr
# import Revit API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
# import Revit Services 
clr.AddReference('RevitServices')

import RevitServices
from RevitServices.Persistence import DocumentManager

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# get the current document in Revit.
doc = DocumentManager.Instance.CurrentDBDocument
# Dynamo input
elements = UnwrapElement(IN[0])
workset = UnwrapElement(IN[1])

# empty lists.
out = list()
    
# loop over elements 
for e in elements:
    # get workset parameter
    wsparam = e.get_Parameter(BuiltInParameter.ELEM_PARTITION_PARAM)
    
    TransactionManager.Instance.EnsureInTransaction(doc)
    #Set the workset
    wsparam.Set(workset.Id)
    out.append(e.WorksetId)
    TransactionManager.Instance.TransactionTaskDone()

OUT = out