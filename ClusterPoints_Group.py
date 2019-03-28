import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *


def groupPoints(point_list,ignore_distance): 
	grouped_points = [] #A list  that contains point groups
	queue = set() #A queue set (contains only unique items)
	while point_list: 
		point_group = [] #A list that contains points that are within the ignore_distance
		queue.add(point_list.pop()) # Move the last point from the point_list to our queue 
		while queue:
			current_point = queue.pop() #Get the last item in the queue and remove it from the queue.
			point_group.append(current_point) #Add the current point to the point_group
			for potential_match in point_list: 
				distance = current_point.DistanceTo(potential_match) 
				if distance <= ignore_distance:
					queue.add(potential_match) 
			point_list = [item for item in point_list if item not in queue] #removes points in queue from point_list

		grouped_points.append(point_group)

	return grouped_points 

OUT = groupPoints(IN[0],IN[1])