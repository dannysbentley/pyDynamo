import clr 

number = 1

string = "this is a string"

MyList = ["item 1", "item 2","item 3",]

MyTuple = ("item 1", "item 2","item 3",)

dict = {"apple" : 2, "orange" : 3, "grape" : 5}

#---------------------------------------------
num = IN[0]

if num > 10:
    OUT = "number is larger than 10"

#---------------------------------------------
num = IN[0]

if num > 10:
    OUT = "number is larger than 10"

else:
    OUT = "number is less than 10"

#---------------------------------------------
num = IN[0]

if num > 10:
    OUT = "number is larger than 10"

elif:
    OUT = "number is larger than 5"

#---------------------------------------------
num = IN[0]

if (num <= 10) and (num >= 0):
    OUT = "number is between 10 and 1"

#---------------------------------------------
num = IN[0]

if (num == 10) or (num == 5):
    OUT = "number is equal to 5 or 10"

#---------------------------------------------
#Dynamo list input 
MyList = IN[0]
#Empty list 
NewList = []

#for each number in my list add one.
for number in MyList:
	#add one and append (add) to my new list
	NewList.append(number + 1)
	
OUT = NewList

#---------------------------------------------
#Empty list 
NewList = []
count = 0
#for each number in my list add one.
while (count <= 9):
    MyList.append(count)
    count = count + 1
	
OUT = NewList


#---------------------------------------------
def addNumbers(number1, number2):
    sumOfNumbers = number1 + number2
    return sumOfNumbers

######################
num1 = IN[0]
num2 = IN[1]

result = addNumbers(num1, num2)

OUT = result

