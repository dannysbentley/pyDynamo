"""
ModifySplitColumns
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
Sample on how to rotate model elements.
Use this sample along with the Video on Youtube.
""" 
import clr
 # import Revit Services 
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# import Revit Nodes 
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
# import Revit API
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

# Import System Collections...
import System
from System.Collections.Generic import *
# get Revit's current document. 
doc =  DocumentManager.Instance.CurrentDBDocument
# add object to a list. 
def tolist(obj1):
    if hasattr(obj1,"__iter__"): return obj1
    else: return [obj1]
 # find level using the level id. 
def FindLevelIndex(levels, lev):
    ind = None
    i = 0
    for l in levels:
        if l.Id.ToString() == lev.Id.ToString():
            ind = i
        i = i+1
    return ind
 # copy level or column and set top and bottom constraints. 
def CopyColByLevel(col, b, t):
    colOut = None
    try:
        c = ElementTransformUtils.CopyElement(doc,col.Id,XYZ(0,0,0))
        c = doc.GetElement(c[0])
        p = c.get_Parameter(BuiltInParameter.FAMILY_BASE_LEVEL_PARAM)
        p.Set.Overloads.Functions[2](b.Id)
        p = c.get_Parameter(BuiltInParameter.FAMILY_TOP_LEVEL_PARAM)
        p.Set.Overloads.Functions[2](t.Id)
        colOut = c.ToDSType(True)
    except Exception, e:
        colOut = e.message
    return colOut
#Dynamo inputs  
run = tolist(IN[0])[0]
cols = tolist(UnwrapElement(IN[1]))
# empty list 
outList = []
if run:
    # get levels using lambda expression 
    levels = list([l for l in FilteredElementCollector(doc).OfClass(Level).ToElements()])
    levels.sort(key=lambda x: x.Elevation, reverse=False)
    # start transaction in Revit. 
    TransactionManager.Instance.EnsureInTransaction(doc)
    for c in cols:
        arr = []
        if c.Category.Name == "Structural Columns":
            p = c.get_Parameter(BuiltInParameter.FAMILY_BASE_LEVEL_PARAM)
            base = doc.GetElement(p.AsElementId())
            p = c.get_Parameter(BuiltInParameter.FAMILY_TOP_LEVEL_PARAM)
            top = doc.GetElement(p.AsElementId())
            
            if not base.Id.IntegerValue == top.Id.IntegerValue:
                i = FindLevelIndex(levels,base)
                j = FindLevelIndex(levels,top)
                
                while i < j:
                    cCopy = CopyColByLevel(c,levels[i], levels[i+1])
                    arr.append(cCopy)    
                    i = i+1
                outList.append(arr)
                doc.Delete(c.Id)
    # transaction end in Revit
    TransactionManager.Instance.TransactionTaskDone()
    OUT = outList
else:
    OUT = "Please Set Run to True"