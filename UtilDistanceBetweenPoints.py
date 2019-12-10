__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

def distance(s, e):
	dist = math.hypot(e.X - s.X, e.Y - s.Y)
	return dist