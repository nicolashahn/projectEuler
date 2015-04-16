# Project Euler
# Nicolas Hahn
# Problem 22

import re

names = sorted(re.findall(r"\w+", open("p022_names.txt","r").read()))
rNames = list(zip(names,[i+1 for i in range(len(names))]))

# character score
def cScore(c):
	return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c)+1

# name score - takes just the name, not rank
def nScore(n):
	return sum([cScore(c) for c in n])

print(sum([nScore(n[0])*n[1] for n in rNames]))