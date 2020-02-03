__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
from Autodesk.Revit.DB import *

# Get the current document from Revit.
doc = DocumentManager.Instance.CurrentDBDocument

#find a level name using the id. 
def FindLevelIndex(levels, levelId):
    lvl = None
    for l in levels:
        if l.Id.ToString() == levelId.ToString():
            lvl = l
    return lvl.Name

#get level 
def getlevel(name, levels):
	for i in levels:
		if i.Name == name:
			return i

#collect all walls in project. 
elements = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
#collect all levels in project. 
levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()

levelNames = []
level = getlevel('Level 1', levels)

for i in elements:
    levelName = FindLevelIndex(levels, i.LevelId)
    levelNames.append(levelName)
	

    