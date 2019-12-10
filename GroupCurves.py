__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *


def groupCurves(Line_List): 
	ignore_distance = 0.1 # Assume points this close or closer to each other are touching 
	Grouped_Lines = [] 
	Queue = set() 
	index = []
	while Line_List: 
		Shape = [] 
		Queue.add(Line_List.pop()) # Move a line from the Line_List to our queue 
		while Queue: 
			Current_Line = Queue.pop()
			Shape.append(Current_Line) 
			for Potential_Match in Line_List: 
				Points = (Potential_Match.StartPoint, Potential_Match.EndPoint)
				for P1 in Points: 
					for P2 in (Current_Line.StartPoint, Current_Line.EndPoint): 
						distance = P1.DistanceTo(P2) 
						if distance <= ignore_distance: 
							Queue.add(Potential_Match) 
			Line_List = [item for item in Line_List if item not in Queue]
		Grouped_Lines.append(Shape) 
	return Grouped_Lines

Curve_Lists = IN[0]

GroupsOut = []

for Curve_List in Curve_Lists:
	Line_List = []
	for c in Curve_List:
		Line_List.append(c.curve)
		
	GroupsOut.append(groupCurves(Line_List))

	
OUT = GroupsOut