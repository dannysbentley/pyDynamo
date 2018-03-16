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
app = doc.Application

#Dynamo input
tempFile = IN[0]
category = IN[1]
#get the category and build a category set. 
builtInCategory = System.Enum.ToObject(BuiltInCategory, category.Id)
cats = app.Create.NewCategorySet()
cats.Insert(doc.Settings.Categories.get_Item(builtInCategory))
#get the parameter file
originalFile = app.SharedParametersFilename
app.SharedParametersFilename = tempFile
sharedParameterFile = app.OpenSharedParameterFile()
#txt group name 
GroupName = sharedParameterFile.Groups.get_Item("DYNAMO AND ADD-IN")
#txt parameter name
externalDefinition = GroupName.Definitions.get_Item("GROUP 1")

#Create shared instance parameter. 
TransactionManager.Instance.EnsureInTransaction(doc)
newInstanceBinding = app.Create.NewInstanceBinding(cats)
doc.ParameterBindings.Insert(externalDefinition, newInstanceBinding, BuiltInParameterGroup.PG_TEXT)
TransactionManager.Instance.TransactionTaskDone()

app.SharedParametersFilename = originalFile