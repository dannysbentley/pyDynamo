"""
CreateSharedParameter
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__version__ = '1.0.0'

"""
Sample on how to create shared parameter.
Use this sample along with the Video on Youtube.
"""
import clr
# import System
import System
from System.Collections.Generic import *
# import Revit API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
# import Revit Services 
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# import Revit API User Interface UI
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
from Autodesk.Revit import Creation
# get the current Revit Document 
doc = DocumentManager.Instance.CurrentDBDocument
# get the user interface document 
uidoc = DocumentManager.Instance.CurrentUIDocument
# get the Revit application. 
app = doc.Application

#Dynamo input
tempFile = IN[0]
category = IN[1]
#get the category and build a category set. 
builtInCategory = System.Enum.ToObject(BuiltInCategory, category.Id)
# create a categroy set incase you need to add to multiple Categories
cats = app.Create.NewCategorySet()
# Add Categories to Category Set. 
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
# Start transaction in Revit. 
TransactionManager.Instance.EnsureInTransaction(doc)
# Create the new shared parameter 
newInstanceBinding = app.Create.NewInstanceBinding(cats)
# insert the new parameter into your project. 
doc.ParameterBindings.Insert(externalDefinition, newInstanceBinding, BuiltInParameterGroup.PG_TEXT)
# complete transaction
TransactionManager.Instance.TransactionTaskDone()
# set back original shared paramter. 
app.SharedParametersFilename = originalFile