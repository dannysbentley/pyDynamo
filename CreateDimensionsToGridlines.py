"""
CreateDimensionsToGridlines
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
Sample on how to create dimensions to gridlines.
Use this sample along with the Video on Youtube.
"""
import clr
# import Revit API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
# import RevitNode 
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)
# import RevitServices
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# Get current document from Revit. 
doc = DocumentManager.Instance.CurrentDBDocument

#Converting input from Dynamo to Revit
line = IN[0].ToRevitType()
grids = UnwrapElement(IN[1])

#Getting refrences from grid
gridRef = ReferenceArray()
opt = Options()
opt.ComputeReferences = True
opt.IncludeNonVisibleObjects = True
opt.View = doc.ActiveView
#loop over grids from input. 
for grid in grids:
	# Get geometry of grids. 
    for obj in grid.get_Geometry(opt):
        if isinstance(obj, Line):
            gline = obj
            gridRef.Append(gline.Reference)

#Create the dimension in a transaction
# Begin transaction with Revit. 
TransactionManager.Instance.EnsureInTransaction(doc)
# create a new dimensions in Revit. 
dim = doc.Create.NewDimension(doc.ActiveView, line, gridRef)
# finish transaction. 
TransactionManager.Instance.TransactionTaskDone()

OUT = dim