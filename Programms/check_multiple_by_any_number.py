#!C:/Users/R4J/AppData/Local/Programs/Python/Python37-32
num = eval(input("Enter number : "))
multiplier = eval(input("Enter multiplier : "))

if (num&multiplier-1)==0 :
	print("The number %d is multiple of %d"%(num,multiplier))
else :
	print("The number %d is not multiple of %d"%(num,multiplier))