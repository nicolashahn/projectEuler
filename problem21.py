# Project Euler
# Nicolas Hahn
# Problem 21

def divSum(n):
	s = 1
	for i in range(2,int(n**0.5)):
		if n%i == 0:
			# print(i,n//i)
			s += i + n//i
	return s

s = 0
for i in range(1,10000):
	n = divSum(i)
	if i == divSum(n) and i != n:
		# print(i,n)
		s += i

print(s)