"""
ModifyGraphicOverride
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
Sample on how to override graphics.
Use this sample along with the Video on Youtube.
""" 
import clr
# import ProtoGeometry 
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
# import Revit Node
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
# import Revit Services 
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# import Revit API
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

#Override graphics 
def OverrideElement(element, color, fill, fillpatt):
	ogs = OverrideGraphicSettings()
	ogs.SetProjectionLinePatternId(fill.Id)
	ogs.SetProjectionFillColor(color)
	ogs.SetProjectionFillPatternId(fillpatt.Id)
	doc.ActiveView.SetElementOverrides(element.Id, ogs)
	
#Convert the Dynamo color to Revit color.
def ConvertColor(element):
	colorList = list()
	for e in element:
		color = Autodesk.Revit.DB.Color(e.Red, e.Green, e.Blue)
		colorList.append(color)
	return colorList
	
doc = DocumentManager.Instance.CurrentDBDocument

#Collect all the line patterns in the project.
patterns = FilteredElementCollector(doc).OfClass(LinePatternElement).ToElements()

fillPatSelected = list()

#search for line pattern
for i in range(len(patterns)):
    namepick = patterns[i].ToDSType(True)
    if namepick.Name == "Dash":
        fillPatSelected.append(patterns[i])
        
elements = UnwrapElement(IN[0]) #Element to change 
colors = ConvertColor(IN[1]) #Color.ByARGB node from Dynamo
fillPat = UnwrapElement(IN[2]) #Fill Pattern node from Dynamo
count = 0 #count to change color if elements are differnt color. 

for i in elements:
    TransactionManager.Instance.EnsureInTransaction(doc)
    #Using def to override graphics. 
    OverrideElement(i, colors[count], fillPatSelected[0], fillPat)
    count += 1
    TransactionManager.Instance.TransactionTaskDone()
	