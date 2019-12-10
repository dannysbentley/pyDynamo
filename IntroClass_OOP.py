"""
FilteredElementCollector
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
Sample on how get elements using a filtered element collector.
Use this sample along with the Video on Youtube.
""" 

class employee():
    def __init__(self, name, title, phone):
        self.name = name
        self.title = title
        self.phone = phone
#create object array to store objects 
employees = []
#create three objects 
emp1 = employee('Jane', 'Architect', '555-0000')
emp2 = employee('Danny', 'Develper', '555-1111')
emp3 = employee('John', 'Jr Developer', '555-2222')
#add objects to array
employees.append(emp1)
employees.append(emp2)
employees.append(emp3)
#print object information from array
for e in employees:
    print(e.name + ', ' + e.title + ', ' + e.phone)
#filter object from array
result = list(filter(lambda e : e.name == "Danny", employees))
print(result[0].name)

#-----------------------------------------------------------

import clr
# import RevitNodes
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
# import Revit Services 
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
# import Revit API
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
# import system.
import System
from System.Collections.Generic import *
# structural columns class 
class StructuralColumn():
	def __init__(self, ElementId, Name, LocationPoint, Workset):
		self.Id = elementId
		self.Name = Name
		self.Location = LocationPoint
		self.Workset = Worket
# get the current Revit document. 
doc = DocumentManager.Instance.CurrentDBDocument
# collect all columns in project 
columns = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralColumns).WhereElementIsNotElementType().ToElements()
# create class object and add informatin to out
out = []
for c in columns:
	ws = doc.GetWorksetTable().GetWorkset(c.WorksetId).Name
    colObj = StructuralColumn(c.Id, c.Name, c.Location, ws)
	out.append(colObj)
	#out.append(c.Location.Point)
	#out.append(c.Name)
	#out.append(c.Id)

#filter out columns by name
result = list(filter(lambda e : e.Name == "C24x24", out))
# send out
OUT = result

#----------------------------------------------------------

import clr

columns = IN[0]
out = []
# print all information 
for c in columns:
	str = c.Name + ', ' + c.Id.ToString() +', '+ c.Workset + ', ' + c.Location.ToString()
	out.append(str)
	
	
OUT = out