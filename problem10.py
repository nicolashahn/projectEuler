# Project Euler
# Nicolas Hahn
# Problem 10

import math

# Sieve of Eratosthenes
def sieve(n):
	A = {}
	for a in range(2,n):
		A[a] = True
	for i in range(2, int(math.ceil(math.sqrt(n)))):
		if A[i] == True:
			j = i*i
			while j < n:
				A[j] = False
				j += i
	result = []
	for p in A:
		if A[p] == True:
			result.append(p)
	return result

print sum(sieve(2000000))
