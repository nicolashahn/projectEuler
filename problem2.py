# Project Euler
# Nicolas Hahn
# Problem 2

def fib(n):
	if n == 0: return 0
	if n == 1: return 1
	return fib(n-1) + fib(n-2)

largest = 0
s = 0
i = 1
while largest <= 4000000:
	largest = fib(i)
	if largest%2 == 0:
		s += largest
	i += 1

print s
