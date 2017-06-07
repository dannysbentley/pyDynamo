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

collector = FilteredElementCollector(doc)
ofClass = collector.OfClass(Wall).ToElements()

ActiveView = FilteredElementCollector(doc, doc.ActiveView.Id).OfClass(Wall).ToElements()

builtInCategory = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()

wallList = []
for w in builtInCategory:
    if w.Name.Equals("SW48"):
        wallList.append(w)

walls = list(filter(lambda x : x.Name.Equals("SW48"), builtInCategory))

builtInCats = List[BuiltInCategory]()
builtInCats.Add(BuiltInCategory.OST_Doors)
builtInCats.Add(BuiltInCategory.OST_Walls)

filter = ElementMulticategoryFilter(builtInCats)

elements = FilteredElementCollector(doc).WherePasses(filter).ToElements()

OUT = ofClass