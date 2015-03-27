# Project Euler
# Nicolas Hahn
# Problem 9

def solution(n):
	for a in range(1,n):
		for b in range(1,n):
			if a + b < n-1:
				c = n - a - b
				if a + b + c == n:
					if (a*a)+(b*b) == (c*c):
						return a*b*c
	return "failed"

print solution(1000)