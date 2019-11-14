import clr 
import System 

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

TYPE = UnwrapElement(IN[0])
#get level 
def getlevel(name, levels):
	for i in levels:
		if i.Name == name:
			return i
			
# create dynamo prototype geometry 
def createDynamoGeometry(x, y, t_z, b_z):
	point_top = Autodesk.DesignScript.Geometry.Point.ByCoordinates(x, y, t_z)
	point_bottom = Autodesk.DesignScript.Geometry.Point.ByCoordinates(x, y, b_z)
	line = Autodesk.DesignScript.Geometry.Line.ByStartPointEndPoint(point_top, point_bottom)
	
	return line, point_top, point_bottom
	
# create Revit Piles 
def createRevitPiles(x, y, t_z, b_z, level, TYPE, SOM_Id):
	point_S = XYZ(x, y, t_z)
	point_E = XYZ(x, y, b_z)
	line_Rvt = Autodesk.Revit.DB.Line.CreateBound(point_S, point_E)
	
	# create Revit Pile elements 
	TransactionManager.Instance.EnsureInTransaction(doc)		
	new_pile = doc.Create.NewFamilyInstance(point_S, TYPE, Structure.StructuralType.NonStructural)
	TransactionManager.Instance.TransactionTaskDone()
	
	# set Revit parameters 
	TransactionManager.Instance.EnsureInTransaction(doc)
	doc.Regenerate()
	p_Depth = new_pile.LookupParameter('Depth')
	p_SOMId = new_pile.LookupParameter('SOM ID')
	p_Depth.Set(b_z)
	p_SOMId.Set(SOM_Id)
	TransactionManager.Instance.TransactionTaskDone()
	
# setup to turn ON and OFF proto geometery and Revit creation. 
def createPiles(row, level, TYPE):
	x = float(row[1])
	y = float(row[2])
	t_z = (float(row[3])-130)-38.75	
	b_z = t_z - float(row[4])
	
	t_z_Rvt = float(row[3]) - 168.75
	b_z_Rvt = float(row[4])
	
	#prototype Dynamo geometry 
	geometry = createDynamoGeometry(x, y, t_z, b_z)
	
	#Revit def to create elements TURN OFF ON FIRST RUN
	createRevitPiles(x, y, t_z_Rvt, b_z_Rvt, level, TYPE, row[0])
	
	return geometry
	
# Main entry for piles 
def piles(rows, level, TYPE):
	geometry = []
	for row in rows[1:]:
		geometry.append(createPiles(row, level, TYPE))
	return geometry
		
# Get the current document from Revit.
doc = DocumentManager.Instance.CurrentDBDocument
# collect all the levels in the Revit model. 
levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()
#get the PILE level 
level = getlevel('PILES', levels)

# read file from path
filepath = "W:/S/BIM/Z-LINKED CSV/PileLocations.csv"
filereader = System.IO.StreamReader(filepath)

# array to collect CSV row data
rows = []
out = []

# loop over items in CSV file. 
while filereader.Peek() > -1:
	line = filereader.ReadLine()
	row = line.Split(",")
	rows.append(row)
	
# close file
filereader.Close()

# Entry to start to create piles. 
out = piles(rows, level, TYPE)

OUT = out