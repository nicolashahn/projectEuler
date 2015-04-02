# Project Euler
# Nicolas Hahn
# Problem 18



t1 = [
[3],
[7, 4],
[2, 4, 6],
[8, 5, 9, 3],
]

t2file = open('p18input','r')
t2 = []

for line in t2file:
	intLine = [int(i) for i in line.split()]
	t2.append(intLine)

# dynamic programming?
# dynamic programming.

def routeSum(t):
	# paths has same number of elements as t, but each will be a path in the form of a list
	paths = []
	for i in range(len(t)):
		paths.append([])
		
		# only one path in that case
		if i == 0:
			paths[i] = [[t[i][0]]]
		
		for j in range(len(t[i])):
			if len(t[i]) > 1:
				
				# leftmost position in row, only one choice
				if j == 0:
					bestPath = list(paths[i-1][0])
				
				# rightmost position, one choice
				elif j == len(t[i])-1:
					bestPath = list(paths[i-1][i-1])
				
				# somewhere inside triangle
				else:
					lpath = list(paths[i-1][j-1])
					rpath = list(paths[i-1][j])
					if sum(lpath) > sum(rpath):
						bestPath = lpath
					else:
						bestPath = rpath

				bestPath.append(t[i][j])
				paths[i].append(bestPath)

	total = max(sum(j) for j in paths[len(paths)-1])
	return total

print routeSum(t2)