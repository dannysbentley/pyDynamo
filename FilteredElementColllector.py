import clr
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

import System
from System.Collections.Generic import *

doc = DocumentManager.Instance.CurrentDBDocument

###  -----------  FilterElementCollector --------------###
#All walls in project
collector = FilteredElementCollector(doc)
wallElements = collector.OfClass(Wall).ToElements()

###  -----------  FilterElementCollector Active View --------------###
#All walls in active view
ActiveView = FilteredElementCollector(doc, doc.ActiveView.Id).OfClass(Wall).ToElements()

###  -----------  FilterElementCollector search for 48" walls --------------###
#collect all walls in Revit then search for SW48
builtInCategory = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()

wallList = []
for w in builtInCategory:
    if w.Name.Equals("SW48"):
        wallList.append(w)

###  -----------  FilterElementCollector lambda expression --------------###
#lambda expression
walls = list(filter(lambda w : w.Name.Equals("SW48"), builtInCategory))

###  -----------  FilterElementCollector using a filter --------------###
#Using a slow filter to get items. 
builtInCat = List[BuiltInCategory]()
builtInCat.Add(BuiltInCategory.OST_Doors)
builtInCat.Add(BuiltInCategory.OST_Walls)

filter = ElementMulticategoryFilter(builtInCats)

elements = FilteredElementCollector(doc).WherePasses(filter).ToElements()

OUT = wallElements