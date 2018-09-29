#!C:/Users/R4J/AppData/Local/Programs/Python/Python37-32
def sumAllEvensInList(numsList) :
	evenNumSum = 0
	for num in numsList :
		if not(num&1) :
			evenNumSum = evenNumSum + num
	return evenNumSum

def main() :
	numsList = eval(input("Enter the list of integer numbers to do the sum of all even numbers : "))
	print("The sum of all even numbers in the list is :", sumAllEvensInList(numsList))

if __name__=='__main__' :
	main()