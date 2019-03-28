# Enable Python support and load DesignScript library
import math
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

class Node:

	def __init__(self, value ,point):
		self.value = value
		self.point = point
		self.parent = ""
		self.H = 0
		self.G = 0
		
	def move_cost(self, other):
		return 0 if self.value == '.' else 1
		
#------------------------------------------------------------------------------------------------
def getAngle(p1, p2):	
	xDiff = p2.X - p1.X
	yDiff = p2.Y - p1.Y
	radian = math.atan2(yDiff, xDiff)
	angle = math.degrees(radian)
	angle = abs(angle)
	angle = round(angle)
	return angle

#using an angle 
def neighbor(current, grid, ignore_distance): 
	current_point = current.point
	grouped_points = []

	for potential_match in grid: 
		distance = current_point.DistanceTo(potential_match.point) 
		a = getAngle(current_point, potential_match.point)
		if distance == 0:
			continue
		if distance <= ignore_distance:
			if a <= 30:
				grouped_points.append(potential_match)	
    return grouped_points

#not using the angle 
def neighbor(current, grid, ignore_distance): 
	current_point = current.point
	grouped_points = []

	for potential_match in grid: 
		distance = current_point.DistanceTo(potential_match.point) 
		if distance == 0:
			continue
		if distance <= ignore_distance:
			grouped_points.append(potential_match)
	
	return grouped_points 
		
#Euclidean distance
def distance(s, e):
	dist = math.hypot(e.point.X - s.point.X, e.point.Y - s.point.Y)
	return dist

#A Star - pathfinding between points 
def aStar(start, goal, grid):
	openset = set()
	closedset = set()
	current = start
	openset.add(current)
	while openset:
		current = min(openset, key=lambda o:o.G + o.H)
		if current == goal:
			path = []
			while current.parent:
				path.append(current)
				current = current.parent
			path.append(current)
			return path[::-1]
			
		openset.remove(current)
		closedset.add(current)
		neighbors = neighbor(current, grid, 1.125)
		for node in neighbors:
			if node in closedset:
				continue
			if node in openset:
				new_g = current.G - distance(current, node)
				if node.G > new_g:
					node.parent = current
			else:
				node.G = current.G - distance(current, node)
				node.H = distance(node, goal)
				node.parent = current
				openset.add(node)
	raise ValueError('No Path Found')

points = IN[0]
nodes = []

for point in points:
	n = Node(points.index(point), point)
	nodes.append(n)

path = aStar(nodes[7], nodes[2089], nodes)

pntsPath = []
out = []
for p in path:
	pnt = p.point
	pntsPath.append(pnt)

for l in range(len(pntsPath)-1,-1,-1):
	line = Line.ByStartPointEndPoint(pntsPath[l], pntsPath[l-1])
	out.append(line)
	
OUT = out