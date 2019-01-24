# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

num = IN[0]
out = []
def x_round(x):
	return round(x*4)/4
	
for n in num:
	out.append(x_round(n).ToString())
OUT = out