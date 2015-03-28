# Project Euler
# Nicolas Hahn
# Problem 12


def factors(n):
	f = []
	for i in range(1, int(n**0.5)+1):
		if n%i == 0:
			f.append(i)
			f.append(n/i)
	return sorted(f)
	
i = 1
t = i
while True:
	if len(factors(t)) > 500:
		print t
		break
	i += 1
	t = t + i
