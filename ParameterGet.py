"""
ParameterGet
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__version__ = '1.0.0'

"""
Sample on how to get a instance and type parameter.
Use this sample along with the Video on Youtube.
"""
import sys
# import Revit API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
# import Revit API UI
clr.AddReference('RevitAPIUI')
# import Revit Services
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager 
# import ProtoGeometry 
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
# get the current Revit Document 
doc = DocumentManager.Instance.CurrentDBDocument
# get the current Revit application
app = DocumentManager.Instance.CurrentUIApplication.Application
# get the current UI application
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
# Dynamo inputs 
elements = IN[0]
parameter = IN[1]
# empty list for output
outList = []
familyType = []
# loop over elements to get instance parameter 
for i in UnwrapElement(elements):
    for j in i.Parameters:
        # Check if instance parameter is shared. 
        if j.IsShared and j.Definition.Name == parameter:
            # check if the instance parameter value if the GUID matches.
            parameterValue = i.get_Parameter(j.GUID)
            outList.append(parameterValue.AsString())

# loop over elements. 
for i in UnwrapElement(IN[0]):
    # get element type.
    id = i.GetTypeId()
    if id == ElementId.InvalidElementId:
        familyType.append(None)
    else:
        familyType.append(doc.GetElement(id))
# get the built in parameter type. 
builtInParamType = BuiltInParameter.ALL_MODEL_TYPE_MARK
# get the type parameter 
for i in UnwrapElement(familyType):
    typeMark = i.get_Parameter(builtInParamType)
    outList.append(typeMark.AsString())

OUT = outList