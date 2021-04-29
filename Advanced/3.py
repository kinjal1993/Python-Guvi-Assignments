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

def printFibonacciSeries(n):
	

	if checkValidNumber(n):
		i = 0
		j = 1
		sum = 0
		n = int(n)
		if n == 1:
			list = [i]
		elif n == 2:
			list = [j]
		else:
			list = [i,j]
		for count in range(n):
			sum = i+j
			list.append(sum)
			i = j
			j = sum
			
		for x in list:
			print(str(x) + "\t")
	else:
		print("Invalid Number")

n = input("Enter number : ")
printFibonacciSeries(n)