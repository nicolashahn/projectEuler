# Project Euler
# Nicolas Hahn
# Problem 6

def sumOfSquares(n):
	result = 0
	for i in range(1,n+1):
		result += i*i
	return result

def squareOfSum(n):
	result = 0
	for i in range(1,n+1):
		result += i
	return result*result

print squareOfSum(100)-sumOfSquares(100)