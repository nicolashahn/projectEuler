# Project Euler
# Nicolas Hahn
# Problem 11

import re
import sys

text = (open('p11input','r')).read()
splitText = re.split('(\d\d)',text)
nums = []
for t in splitText:
	if t != ' ' and t != '' and t != '\n':
		nums.append(int(t))
rows = [[0 for i in range(20)] for i in range(20)]

rIndex = 0
for r in rows:
	for i in range(20):
		r[i] = (nums[rIndex*20+i])
	rIndex += 1

# now we finally have a two dimensional array

def product(list):
    p = 1
    for i in list:
        p *= i
    return p

# adj = # of adjacent numbers to check product of
# matrix = list of lists of ints
def verts(adj,matrix):
	maxProd = 0
	for i in range(len(matrix)-adj+1):
		currList = []
		for j in range(adj):
			currList.append(matrix[i][j])
		if maxProd < product(currList):
			maxProd = product(currList)
	return maxProd

def horizontals(adj, matrix):
	maxProd = 0
	for i in range(len(matrix)):
		for j in range(len(matrix)-adj+1):
			currList = []
			for k in range(adj):
				currList.append(matrix[i][j+k])
		if maxProd < product(currList):
			maxProd = product(currList)
	return maxProd

def ldiags(adj, matrix):
	maxProd = 0
	for i in range(len(matrix)-adj+1):
		for j in range(len(matrix)-adj+1):
			currList = []
			for k in range(adj):
				currList.append(matrix[i+k][j+k])
			if maxProd < product(currList):
				maxProd = product(currList)
	return maxProd

def rdiags(adj, matrix):
	maxProd = 0
	for i in range(len(matrix)-adj+1):
		for j in range(adj,len(matrix)):
			currList = []
			for k in range(adj):
				currList.append(matrix[i+k][j-k])
			if maxProd < product(currList):
				maxProd = product(currList)
	return maxProd

print max(verts(4,rows),horizontals(4,rows),ldiags(4,rows),rdiags(4,rows))