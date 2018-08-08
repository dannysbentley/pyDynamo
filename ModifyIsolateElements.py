"""
ModifyIsolateElements
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__version__ = '1.0.0'

"""
Sample on how to isolate elements and turn off all other elements in view.
Use this sample along with the Video on Youtube.
""" 
import clr
# Import Revit Services 
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# Import Revit API
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
# Import System
import System
from System.Collections.Generic import *
# get the current Revit document
doc = DocumentManager.Instance.CurrentDBDocument
# filter element collector of wall in active view. 
ActiveViewElements = FilteredElementCollector(doc, doc.ActiveView.Id).OfClass(Wall).ToElements()
# unwrap elements
elements = UnwrapElement(ActiveViewElements)
view = UnwrapElement(doc.ActiveView)
# empty list
ids = list()
# loop over each elmeent and get the Id. 
for items in elements:
    ids.append(items.Id)
# add to list 
idElements = List[ElementId](ids)
# start transcation in Revit. 
TransactionManager.Instance.EnsureInTransaction(doc)
# isolate elements
view.IsolateElementsTemporary(idElements)
# complete transcation in Revit. 
TransactionManager.Instance.TransactionTaskDone()