# Project Euler
# Nicolas Hahn
# Problem 5

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

def divBy(n, m):
	for i in range(0,m-1):
		if n%(m-i) != 0:
			return (m-i)
	return True

f = []
for i in range(2,20):
	for factor in factors(i):
		if factor not in f:
			f.append(factor)
print f
f = [2,2,2,3,5,7,11,13,17,19]
s = reduce(lambda x, y: x*y, f)
print s