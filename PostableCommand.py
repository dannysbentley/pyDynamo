"""
PostableCommand
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
UnderConstruction - still hasn't been developed. 
Use this sample along with the Video on Youtube.
"""
import clr
import System

from System.Collections.Generic import *

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
from Autodesk.Revit import Creation


doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIDocument
uiapp = DocumentManager.Instance.CurrentUIApplication

ClientId = "8a6ec64e-8641-41ff-a518-932a470b297e"

# Get RevitCommandId of PostableCommand...
rvtComId = RevitCommandId.LookupCommandId(ClientId)
post = uiapp.CanPostCommand(rvtComId)

# Run PostableCommand...
#uiapp.PostCommand(rvtComId)

OUT = post