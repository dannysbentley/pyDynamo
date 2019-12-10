"""
ModifyColor
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
Sample on how to change color using graphic override.
Use this sample along with the Video on Youtube.
""" 
import clr
# import ProtoGeometry
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
# import RevitNode
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
# import RevitServices
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# import Revit API
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
# get the current Revit current document. 
doc = DocumentManager.Instance.CurrentDBDocument
# convert Dynamo color to Revit color. 
def ConvertColor(element):
	return Autodesk.Revit.DB.Color(element.Red, element.Green, element.Blue)
# override definition 
def OverrideElement(element, color, fill):
	# get the override setting
	ogs = OverrideGraphicSettings()
	# override fill of color 
	ogs.SetProjectionFillColor(color)
	# set the fill pattern
	ogs.SetProjectionFillPatternId(fill.Id)
	# set fill cut fill color
	ogs.SetCutFillColor(color)
	# set cut fill pattern 
	ogs.SetCutFillPatternId(fill.Id)
	doc.ActiveView.SetElementOverrides(element.Id, ogs)
# Dynamo input 
elements = UnwrapElement(IN[0])
colors = ConvertColor(IN[1])
fillPat = UnwrapElement(IN[2])
# loop over elements 
for i in elements:
	# start transaction in Revit
    TransactionManager.Instance.EnsureInTransaction(doc)
	# override element in Revit. 
    OverrideElement(i, colors, fillPat)
	# complete transaction in revit. 
    TransactionManager.Instance.TransactionTaskDone()