#!C:/Users/R4J/AppData/Local/Programs/Python/Python37-32
num = eval(input("Enter eatable donuts number : "))

if num<0 :
	print("No donuts ate")
elif num<=2 :
	print("Too few donuts ate")
elif num<=10 :
	print("Number of donuts ate :",str(num))
elif num>10 :
	print("Number of donuts too many")