#!C:/Users/R4J/AppData/Local/Programs/Python/Python37-32
side1 = eval(input("Enter first side : "))
side2 = eval(input("Enter second side : "))
side3 = eval(input("Enter third side : "))

if (side1>side2 or side1<side2) :
	if (side2>side3 or side2<side3) :
		print("This side values can form triangle")
	else :
		print("This side values can not form triangle")