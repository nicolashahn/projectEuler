# Project Euler
# Nicolas Hahn
# Problem 14

def collatz(ct,n):
	ct+=1
	if n!=1:
		if n % 2 == 0:
			return collatz(ct, n/2)
		else:
			return collatz(ct, 3*n+1)
	else:
		return ct

bestCt = 0
bestn = 0
for n in range(1,1000000):
	thisCt = collatz(0,n)
	if thisCt > bestCt: 
		bestCt = thisCt
		bestn = n
print bestn
