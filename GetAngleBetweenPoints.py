__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

import clr
import math
clr.AddReference('RevitAPI')
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference("RevitNodes")
import Revit

def getAngle(p1, p2):	
	xDiff = p2.X - p1.X
	yDiff = p2.Y - p1.Y
	radian = math.atan2(yDiff, xDiff)
	angle = math.degrees(radian)
	angle = abs(angle)
	angle = round(angle)
	return angle

def getLocationCurve(loc):
	return loc.Curve.ToProtoType()
def getLocationPoint(loc):
	return loc.Point.ToPoint()