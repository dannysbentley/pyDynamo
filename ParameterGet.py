import clr
import sys

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager 

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

doc = DocumentManager.Instance.CurrentDBDocument
app = DocumentManager.Instance.CurrentUIApplication.Application

uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

elements = IN[0]
parameter = IN[1]

outList = []
familyType = []

for i in UnwrapElement(elements):
    for j in i.Parameters:
        if j.IsShared and j.Definition.Name == parameter:
            parameterValue = i.get_Parameter(j.GUID)
            outList.append(parameterValue.AsString())

for i in UnwrapElement(IN[0]):
    id = i.GetTypeId()
    if id == ElementId.InvalidElementId:
        familyType.append(None)
    else:
        familyType.append(doc.GetElement(id))

builtInParamType = BuiltInParameter.ALL_MODEL_TYPE_MARK

for i in UnwrapElement(familyType):
    typeMark = i.get_Parameter(builtInParamType)
    outList.append(typeMark.AsString())

OUT = outList