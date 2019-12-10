__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'


import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

import System
from System.Collections.Generic import *

import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)

# def to export
def ExportDwg(doc, path, fileName, view, options):
	#Empty List to add ids
	views = List[ElementId]()
	#Convert list to Element Id list. 
	for v in view:
		views.Add(v.Id) #add view Ids.
	#Set combined set to true. 
	options.MergedViews = True
	#The export from Document to AutoCAD files.
	result = doc.Export(path, fileName[1], views, options)
	
	return result
	
#inputs 
path = IN[0] # input file path
fileName = IN[1] # input file name
view = UnwrapElement(IN[2]) # input Sheets
options = IN[3] # input company option.

#Revit Document
doc = DocumentManager.Instance.CurrentDBDocument

#run def
result = ExportDwg(doc, path, fileName, view, options)

OUT = result