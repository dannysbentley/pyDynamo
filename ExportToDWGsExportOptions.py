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

doc = DocumentManager.Instance.CurrentDBDocument
options = None
#check if the dwg export setting matches this name
dwg_opt = "- SOM Struc Export"
#collect all the settings in your project.
settings = FilteredElementCollector(doc).WherePasses(ElementClassFilter(ExportDWGSettings))

for element in settings:
	if element.Name == dwg_opt:
		options = element.GetDWGExportOptions()
		break
if options is None:
	options = DWGExportOptions()
	
	
OUT = options