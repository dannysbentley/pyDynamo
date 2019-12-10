"""
RegexSearch
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
Sample on how search and replace test using Regex.
Use this sample along with the Video on Youtube.
"""
import clr
import re
# Dynamo input
regexString = IN[0]
SheetNameList = IN[1]
# empty list
elementList = list()
# loop over sheets 
for item in SheetNameList:
	# search text and replace using Regex 
	searchObj = re.search(regexString, item)
	# add to list
	elementList.append(searchObj.group())

OUT = elementList