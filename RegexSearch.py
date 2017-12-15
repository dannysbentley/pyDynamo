import clr
import re

regexString = IN[0]
SheetNameList = IN[1]

elementList = list()

for item in SheetNameList:
	searchObj = re.search(regexString, item)
	elementList.append(searchObj.group())

OUT = elementList