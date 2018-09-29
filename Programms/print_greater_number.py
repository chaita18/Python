#!C:/Users/R4J/AppData/Local/Programs/Python/Python37-32
num1 = eval(input("Enter first number : "))
num2 = eval(input("Enter second number : "))
num3 = eval(input("Enter third number : "))

if num1>num2 and num1>num3 :
	print("%d is the greatest number"%num1)
elif num2>num3 :
	print("%d is the greatest number"%num2)
else :
	print("%d is the greatest number"%num3)