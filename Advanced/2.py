#Write a code using a function to check whether a given number is prime number or not
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

def checkPrimeNumber(number):
	isPrimeNumber = True
	if checkValidNumber(number):
		if number == 1:
			print("Number is 1")
		else:
			for d in range(2,number):
				if number % d == 0:
					isPrimeNumber = False
					break
		if isPrimeNumber:
			print(str(number) + " is a prime number")
		else:
			print(str(number) + " is not a prime number")
	else:
		print("Invalid Number")

checkPrimeNumber(2)
checkPrimeNumber(1)
checkPrimeNumber(32)