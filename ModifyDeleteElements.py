"""
ModifyDeleteElements
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
Sample on how to delete model elements.
Use this sample along with the Video on Youtube.
""" 
import clr
# Import Revit Services 
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# get the current Revit document 
doc = DocumentManager.Instance.CurrentDBDocument
# Dynamo inputs 
elements = UnwrapElement(IN[0])
# start Revit transaction 
TransactionManager.Instance.EnsureInTransaction(doc)
# loop over each element to delete. 
for e in elements:
    doc.Delete(e.Id)
# finish transcation in Revit. 
TransactionManager.Instance.TransactionTaskDone()

OUT = "done"