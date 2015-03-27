# Project Euler
# Nicolas Hahn
# Problem 3

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

num = 600851475143

print max(factors(num))


# print [prime(i) for i in factors(num)]