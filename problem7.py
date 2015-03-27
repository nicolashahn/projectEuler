# Project Euler
# Nicolas Hahn
# Problem 7

primes = []
i = 2
while True:
	iPrime = True
	for p in primes:
		if i%p == 0:
			iPrime = False
			break
	if iPrime == True:
		primes.append(i)
	i += 1
	if len(primes) == 10001:
		break
print primes[10000]