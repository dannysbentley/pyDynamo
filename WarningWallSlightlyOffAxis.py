"""
WarningWallSlightlyOffAxis
"""
__author__ = 'Danny Bentley - danny.b@dwp.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
This is a dynamo script to fix the warning for
walls that are slightly off axis. 
""" 
import clr
#import ProtoGeometry
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
# import Revit Servies 
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# import Revit Nodes 
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
# import Revit API
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
# import system
clr.AddReference("System")
from System.Collections.Generic import *
# get current Revit document. 
doc = DocumentManager.Instance.CurrentDBDocument
# Dynamo inputs
elements = UnwrapElement(IN[0])

# definition to get the wall curve 
def getWallCurve(e):
	loc = e.Location
	if loc.ToString() == 'Autodesk.Revit.DB.LocationCurve':
		return loc.Curve
	
def wallPointStart(e):
	loc = e.Location
	if loc.ToString() == 'Autodesk.Revit.DB.LocationCurve':
		l = e.Location
		lc = l.Curve	
		return lc.GetEndPoint(0)

#Point location at end
def wallPointEnd(e):
	loc = e.Location
	if loc.ToString() == 'Autodesk.Revit.DB.LocationCurve':
		l = e.Location
		lc = l.Curve	
		return lc.GetEndPoint(1)
		
def getMargin(e):
	loc = e.Location
	if loc.ToString() == 'Autodesk.Revit.DB.LocationCurve':
		margin = loc.Curve.Length / 5000
		return margin
		
def moveWall(e, newLocation):
	try:
		# start transaction in Revit
		TransactionManager.Instance.EnsureInTransaction(doc)
		# move elements to new location. 
		e.Location.Curve = newLocation
		# end transcation in Revit. 
		TransactionManager.Instance.TransactionTaskDone()
	except:
		out.append('error')

out = []
for e in elements:
	margin = getMargin(e)
	cS = wallPointStart(e)
	cE = wallPointEnd(e)
	if cS != None:
		dX = abs(cS.X - cE.X)
		dY = abs(cS.Y - cE.Y)
		out.append(dX)
		if(dX <= margin):
			xyzS = XYZ(cS.X, cS.Y, cS.Z)
			xyzE = XYZ(cE.X, cE.Y, cE.Z)
			newLocation = Autodesk.Revit.DB.Line.CreateBound(xyzS, XYZ(cS.X, cE.Y, cE.Z))
			moveWall(e, newLocation)
			out.append(e.Id)
		
		if(dY <= margin):
			xyzS = XYZ(cS.X, cS.Y, cS.Z)
			xyzE = XYZ(cE.X, cE.Y, cE.Z)
			newLocation = Autodesk.Revit.DB.Line.CreateBound(xyzS, XYZ(cE.X, cS.Y, cE.Z))
			moveWall(e, newLocation)
			out.append(e.Id)
OUT = out
