"""
ModifyChangeFamilyType
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__version__ = '1.0.0'

"""
Sample on how to change family type.
Use this sample along with the Video on Youtube.
""" 
import clr
# Import Revit API
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
# Import Revit Services 
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# Get the current Revit document. 
doc = DocumentManager.Instance.CurrentDBDocument
#Dynamo input 
familyInstance = UnwrapElement(IN[0]) # elements 
familyType = UnwrapElement(IN[1]) # type 
count = 0 # count
# Begin Revit transaction.
TransactionManager.Instance.EnsureInTransaction(doc)
# loop over each element 
for item in familyInstance:
    # Change Revit Element. 
    item.Symbol = familyType
    count += 1
# end transaction. 
TransactionManager.Instance.TransactionTaskDone()
