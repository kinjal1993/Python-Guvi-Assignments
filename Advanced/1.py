#Write a code using a function to check whether a given number is even or odd
def checkValidNumber(number):
	error = False
	if number is None:
		error = True
	else:
		try:
			number = int(number)
			if number == 0:
				error = True
		except ValueError:
			error = True
	return not error
    
def checkNumberOddEven(number):
	if checkValidNumber(number):
		if number % 2 == 0:
			number_type = "even"
		else:
			number_type = "odd"
		print("Number is "+number_type)
	else:
		print("Invalid Number")

checkNumberOddEven(5)
checkNumberOddEven(6)
checkNumberOddEven(0)