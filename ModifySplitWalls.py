import clr
 
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc =  DocumentManager.Instance.CurrentDBDocument
 
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
 
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
 
import System
from System.Collections.Generic import *
 
############## Definitions Start ##############
# Convert to List if singleton...
def tolist(obj1):
    if hasattr(obj1,"__iter__"): return obj1
    else: return [obj1]
     
# Returns the index of the found level given a Level and a list of Levels...
def FindLevelIndex(levels, lev):
    ind = None
    i = 0
    for l in levels:
        if l.Id.ToString() == lev.Id.ToString():
            ind = i
        i = i+1
    return ind
 
# Copy the original wall and set it's levels using the Built-In Parameters for the Base and Top Constraints...
def CopyWallByLevel(wall, b, t):
    wallOut = None
    try:
        # Copy the Original Wall with a transformation vector of 0,0,0...
        w = ElementTransformUtils.CopyElement(doc,wall.Id,XYZ(0,0,0))
        # Since the CopyElements method returns the ElementId of the new wall we need to get this Element from the Document...
        w = doc.GetElement(w[0])
        # Update the Base and Top constraints Parameters using the Built-In Parameters.
        # Note: I have explicitly chosen the Overload as I was getting flaky behaviour where the wrong overload was being used...
        p = w.get_Parameter(BuiltInParameter.WALL_BASE_CONSTRAINT)
        p.Set.Overloads.Functions[2](b.Id)
        p = w.get_Parameter(BuiltInParameter.WALL_HEIGHT_TYPE)
        p.Set.Overloads.Functions[2](t.Id)
        wallOut = w.ToDSType(True)
    # Write out any exceptions...
    except Exception, e:
        wallOut = e.message
    # Return new wall..
    return wallOut    
############## Definitions End ##############
 
# IN-Variables...
run = tolist(IN[0])[0]
walls = tolist(UnwrapElement(IN[1]))
 
# OUT-Variables...
outList = []
 
# Main Script...
# Test if user has selected Run as True...
if run:
    # Get All Levels in the Document and cast to .net List...
    levels = list([l for l in FilteredElementCollector(doc).OfClass(Level).ToElements()])
    # Sort Levels by Elevation using a lamda expression...
    levels.sort(key=lambda x: x.Elevation, reverse=False)
     
    # Start a new Transaction ready for modifying the Document...
    TransactionManager.Instance.EnsureInTransaction(doc)
    for w in walls:
        arr = []
        # Check if the Element is a Wall...
        if w.GetType() == Wall:
            # Get Base and Top Constraints as Levels...
            p = w.get_Parameter(BuiltInParameter.WALL_BASE_CONSTRAINT)
            base = doc.GetElement(p.AsElementId())
            p = w.get_Parameter(BuiltInParameter.WALL_HEIGHT_TYPE)
            top = doc.GetElement(p.AsElementId())
            
            # Test whether walls Base and Top levels are NOT the same, if they are we will skip this wall, if they are not then we will get the Index of the Level in the sorted list of Levels we collected earlier for both the Base and Top of the wall...
            if not base.Id.IntegerValue == top.Id.IntegerValue:
                # Note: we are setting the bounds of the Loop below with the Indices of the found Levels so we will only loop through the Levels in between the Base and Top Levels...            
                i = FindLevelIndex(levels,base)
                j = FindLevelIndex(levels,top)
                
                # Loop through the Levels between the Base and Top Levels copying the original wall for each iteration and stepping up one Level...
                while i < j:
                    wCopy = CopyWallByLevel(w,levels[i], levels[i+1])
                    arr.append(wCopy)    
                    i = i+1
                outList.append(arr)
                # Delete original Wall as this has now been split by Level...
                doc.Delete(w.Id)
    # End the Transaction...
    TransactionManager.Instance.TransactionTaskDone()
    # Return the new Walls...
    OUT = outList
# Return if user has not set input Run to True...
else:
    OUT = "Please Set Run to True"