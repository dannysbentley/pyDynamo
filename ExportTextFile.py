"""
ExportTextFile
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__version__ = '1.0.0'

"""
Export data to a text file. 
"""
import clr
# import system. 
import System
# get file path to write file. 
filepath = IN[0]
# data as list
dataList = IN[1]
# write to file stream
file = System.IO.StreamWriter(filepath)
# write line 
# List of elements
for data in dataList:
    #List of parameters
	for d in data:
        #string builder by joining
        # formatting and converting to string.
		sb = ','.join(['"{}"'.format(str(d)) for d in data])
    #write line to file
	file.WriteLine(sb)

#close and dispose of file. 
file.Close()
file.Dispose()
	
OUT = sb