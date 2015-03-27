# Project Euler
# Nicolas Hahn
# Problem 5

from fractions import gcd

def lcm(a,b):
	return a*b/gcd(a,b)

print reduce(lambda x, y: lcm(x,y), range(1,20))