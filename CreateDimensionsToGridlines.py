import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

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
for grid in grids:
    for obj in grid.get_Geometry(opt):
        if isinstance(obj, Line):
            gline = obj
            gridRef.Append(gline.Reference)

#Create the dimension in a transaction
TransactionManager.Instance.EnsureInTransaction(doc)

dim = doc.Create.NewDimension(doc.ActiveView, line, gridRef)

TransactionManager.Instance.TransactionTaskDone()

OUT = dim