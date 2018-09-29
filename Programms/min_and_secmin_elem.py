#!C:/Users/R4J/AppData/Local/Programs/Python/Python37-32
def minSecondMin(numsList) :
	if numsList == None :
		return
	elif len(numsList) == 1 :
		return numsList[0], None
	else :
		minimum = numsList[0]
		secmin = numsList[1]
		if secmin < minimum :
			minimum = numsList[1]
			secmin = numsList[0]

		for num in numsList[2:] :
			if num < minimum :
				secmin = minimum
				minimum = num
			elif num < secmin :
				secmin = num
	return minimum, secmin


def main() :
	numsList = eval(input("Enter the list of integer to get the minimum and second minimum element in the list : "))
	print("The minimum and second minimum number in the list :", minSecondMin(numsList))

if __name__=='__main__' :
	main()