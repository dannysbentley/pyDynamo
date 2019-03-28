def getAngle(p1, p2):	
	xDiff = p2.X - p1.X
	yDiff = p2.Y - p1.Y
	radian = math.atan2(yDiff, xDiff)
	angle = math.degrees(radian)
	angle = abs(angle)
	angle = round(angle)
	return angle