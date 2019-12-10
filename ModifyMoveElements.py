"""
ModifyMoveElements
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
Sample on how to move model elements.
Use this sample along with the Video on Youtube.
""" 
import clr
# import Revit servies 
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# import Revit nodes
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
# import Revit API
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
# import system. 
clr.AddReference("System")
from System.Collections.Generic import *

# get the current Revit Document.
doc = DocumentManager.Instance.CurrentDBDocument
# Dynamo inputs 
elements = UnwrapElement(IN[0])
newLocation = IN[1].ToXyz()
# empty list of element ids 
Ids = List[ElementId]()
# loop over elements and get id
for e in elements:
    Ids.Add(e.Id)
# start transaction in Revit. 
TransactionManager.Instance.EnsureInTransaction(doc)
# move elements to new location. 
ElementTransformUtils.MoveElements(doc, Ids, newLocation)
# end transcation in Revit. 
TransactionManager.Instance.TransactionTaskDone()

OUT = Ids