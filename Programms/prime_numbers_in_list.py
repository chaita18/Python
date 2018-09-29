#!C:/Users/R4J/AppData/Local/Programs/Python/Python37-32
def isPrimeNumInList(numsList) :
	primeListNum = []
	for num in numsList :
		if num < 2 :
			pass
		elif num ==2 or num == 3 :
			pass
		elif num % 2 == 0 :
			pass
		else :
			flag = False
			for x in range(3, num) :
				if num % 3 == 0 :
					pass
				else :
					flag = True

			if flag == True :
				primeListNum.append(num)

	return primeListNum

def main() :
	numsList = eval(input("Enter the list of integer  : "))
	print("The list of prime numbers :", isPrimeNumInList(numsList))

if __name__=='__main__' :
	main()