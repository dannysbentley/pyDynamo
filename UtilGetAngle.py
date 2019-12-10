__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

def getAngle(p1, p2):	
	xDiff = p2.X - p1.X
	yDiff = p2.Y - p1.Y
	radian = math.atan2(yDiff, xDiff)
	angle = math.degrees(radian)
	angle = abs(angle)
	angle = round(angle)
	return angle