# Project Euler
# Nicolas Hahn
# Problem 20

# time for more DP

import math

'''
f = {}

def mfactorials(n):
	if n == 1:
		return 1
	if n in f:
		return f[n]
	else:
		res = 1
		for i in range(1,n):
			res *= mfactorials(i)
		f[n] = res
		return res

print mfactorials(10)
print math.factorial(100)
'''

solution = sum([int(s) for s in str(math.factorial(100))])

print solution