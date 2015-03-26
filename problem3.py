# Project Euler
# Nicolas Hahn
# Problem 3

def prime(n):
	for i in range(2,n-1):
		if n%i == 0:
			return False
	return True

def isFactor(f,n):
	if n%f == 0:
		return True
	return False

def factorRemainder(f,n):
	if isFactor(f,n):
		return n/f


def factors(num):
	f = []
	i = 2
	n = num
	while n/i > 1:
		if n%i == 0:
			f.append(i)
			for e in factors(n/i):
				f.append(e)
			n = n/i
		i += 1
		if i*i > n:
			if n>1: f.append(n)
			break
	return f


print max(factors(num))


# print [prime(i) for i in factors(num)]