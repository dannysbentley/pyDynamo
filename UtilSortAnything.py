import clr
import operator
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
import System
from System.Collections.Generic import *

def sortDict(keys, values):
	sorted_values = []
	dict = {key:value for key, value in zip(keys, values)}
	sorted_pair = sorted(dict.items(), key=operator.itemgetter(0))
	for value in sorted_pair:
		sorted_values.append(value[1])
	return sorted_values


#also can use this 
list = sorted(input, key = lambda p : (p.X))