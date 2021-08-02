# Enable Python support and load DesignScript library
import clr
import System
		
# read file from path
filepath = "C:/Users/DWP/Downloads/Import Sheets - Sheet1.csv"
filereader = System.IO.StreamReader(filepath)

number = []
name = []

# loop over items in CSV file. 
while filereader.Peek() > -1:
	line = filereader.ReadLine()
	row = line.Split(",")
	number.append(row[0])
	name.append(row[1])
	
# close file
filereader.Close()
	
OUT = number, name