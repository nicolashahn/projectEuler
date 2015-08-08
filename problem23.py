import math

def divisors(n):
	yield 1
	largest = int(math.sqrt(n))
	if largest*largest == n:
		yield largest
	else:
		largest += 1
	for i in range(2,largest):
		if n%i == 0:
			yield i
			yield n/i

def isAbundant(n):
	if n < 12:
		return False
	return sum(divisors(n)) > n

def isSumOfAbundants(n, abundants):
	smallerThanNAbundants = [j for j in abundants if j < n]
	for i in smallerThanNAbundants:
		if n-i in smallerThanNAbundants:
			return True
	return False

abundants = [i for i in range(1,23124) if isAbundant(i)]

print(sum([i for i in range(1,23124) if not isSumOfAbundants(i, abundants)]))