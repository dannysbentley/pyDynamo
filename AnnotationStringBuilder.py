import clr
"""
AnnotationStringBuilder
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
Sample on how to build up a string using input from Revit.
I used this to build up a parameter with depth and width 
to then be tagged using an annotation. 
"""
import System
#input for depth and width
depth = IN[0]
width = IN[1]
#empty list to out
out = []
#use count for two list
count = 0
#check if number is whole
def is_whole(n):
    if n%2 == 0 or (n+1)%2 == 0:
        return int(round(n))
    else:
        return n
#loop over depth 
for d in depth:
	#check number if it's whole
	d = is_whole(d)
	#convert to string 
	d = str(d)
	#get item from index of width
	w = width[count]
	#check if nujmber is a whole
	w = is_whole(w)
	#convert to string. 
	w = str(w)
	#build string for annotation.
	sb = d + 'X' + w
	#add to list 
	out.append(sb)
	#advance count for index. 
	count = count + 1
	
#send out
OUT = out