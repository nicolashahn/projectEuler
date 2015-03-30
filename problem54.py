# Nicolas Hahn
# Project Euler
# Problem 54

import re

cards = re.split('\s',open('poker.txt','r').read())

p1cards = []
p2cards = []

for i in range(len(cards)/10):
	for j in range(0,5):
		p1cards.append(cards[i*10+j])
	for j in range(5,10):
		p2cards.append(cards[i*10+j])

value = {
	'2':2,
	'3':3,
	'4':4,
	'5':5,
	'6':6,
	'7':7,
	'8':8,
	'9':9,
	'T':10,
	'J':11,
	'Q':12,
	'K':13,
	'A':14,
}

h1 = ['TC','9C','8C','7C','6C']
h2 = ['TC','TC','TC','TC','AC']

def getHand(cards):
	return [cards.pop(0) for i in range(5)]

def handValues(hand):
	return [value[x[0]] for x in hand]

'''
def popHighCard(hand):
	maxValue = 0
	bestCard = -1
	i = 0
	for x in hand:
		if value[x[0]] > maxValue:
			maxValue = value[x[0]]
			bestCard = i
		i += 1
	return hand.pop(bestCard)
'''

# return value of highest value card in hand
def popHighCard(hand):
	s = sorted(handValues(hand))
	print s
	return s.pop()

'''
def onePair(hand):
	v = handValues(hand)
	for i in range(len(v)):
		for j in range(len(v)):
			if v[i] == v[j] and i != j:
				return True
	return False
'''

def onePair(hand):
	seen = []
	for x in handValues(hand):
		if x in seen:
			return True
		else:
			seen.append(x)
	return False

def onePairValue(hand):
	seen = []
	for x in handValues(hand):
		if x in seen:
			return x
		else:
			seen.append(x)
	return 0

def twoPair(hand):
	seen = []
	pairs = []
	for x in handValues(hand):
		if x in seen and x not in pairs:
			pairs.append(x)
		else:
			seen.append(x)
	return len(pairs) >= 2

def twoPairValue(hand):
	seen = []
	pairs = []
	for x in handValues(hand):
		if x in seen and x not in pairs:
			pairs.append(x)
		else:
			seen.append(x)
	if len(pairs) >= 2:
		return max(pairs)
	else:
		return 0

def threeOfAKind(hand):
	seen = []
	pairs = []
	for x in handValues(hand):
		if x in seen and x not in pairs:
			pairs.append(x)
		elif x in seen and x in pairs:
			return True
		else:
			seen.append(x)
	return False

def threeOfAKindValue(hand):
	seen = []
	pairs = []
	for x in handValues(hand):
		if x in seen and x not in pairs:
			pairs.append(x)
		elif x in seen and x in pairs:
			return x
		else:
			seen.append(x)
	return 0

def straight(hand):
	s = sorted(handValues(hand))
	for i in range(len(s)-1):
		if s[i]+1 != s[i+1]:
			return False
	return True

def straightValue(hand):
	s = sorted(handValues(hand))
	for i in range(len(s)-1):
		if s[i]+1 != s[i+1]:
			return 0
	return max(s)
	

def flush(hand):
	for x in hand:
		if x[1] != hand[0][1]:
			return False
	return True

def fullHouse(hand):
	seen = []
	dupes = []
	for x in handValues(hand):
		if x in seen and x not in dupes:
			dupes.append(x)
		if x not in seen:
			seen.append(x)
	return len(dupes) == 2

def fullHouseValue(hand):
	seen = []
	dupes = []
	for x in handValues(hand):
		if x in seen and x in dupes:
			triple = x
		if x in seen and x not in dupes:
			dupes.append(x)
		if x not in seen:
			seen.append(x)
	if len(dupes) == 2:
		return triple
	else:
		return 0

def fourOfAKind(hand):
	seen = []
	dupes = []
	ct = 0
	for x in handValues(hand):
		if x in seen and x not in dupes:
			dupes.append(x)
		if x not in seen:
			seen.append(x)
		if x in dupes:
			ct += 1
	return ct == 3 and len(dupes) == 1 

def fourOfAKindValue(hand):
	seen = []
	dupes = []
	ct = 0
	for x in handValues(hand):
		if x in seen and x not in dupes:
			dupes.append(x)
		if x not in seen:
			seen.append(x)
		if x in dupes:
			ct += 1
	if ct == 3 and len(dupes) == 1:
		return dupes[0]
	else:
		return 0

def straightFlush(hand):
	return flush(hand) and straight(hand)

def straightFlushValue(hand):
	if flush(hand):
		return straight(hand)

def royalFlushValue(hand):
	return sorted(handValues(hand)) == [10,11,12,13,14] and flush(hand)


def royalFlushValue(hand):
	if sorted(handValues(hand)) == [10,11,12,13,14] and flush(hand):
		return 14
	else:
		return 0

def handRank(hand):
	if royalFlushValue(hand):
		return 10
	elif straightFlush(hand):
		return 9
	elif fourOfAKind(hand):
		return 8
	elif fullHouse(hand):
		return 7
	elif flush(hand):
		return 6
	elif straight(hand):
		return 5
	elif threeOfAKind(hand):
		return 4
	elif twoPair(hand):
		return 3
	elif onePair(hand):
		return 2
	else:
		return 1

def rankToFunction(hand, rank):
	if rank == 10:
		return 

def breakTie(h1, h2, f):
	return f(h1) > f(h2)

# check the highest ranked hand for each player
# if tie, highest non tied card wins
def p1wins(h1, h2):
	if handRank(h1) > handRank(h2):
		return True
	elif handRank(h1) < handRank(h2):
		return False
	elif handRank(h1) == handRank(h2) and handRank(h1) != 1:
		if royalFlushValue(h1) != royalFlushValue(h2) and royalFlushValue:
			return royalFlushValue(h1) > royalFlushValue(h2)
		elif straightFlushValue(h1) != straightFlushValue(h2):
			return straightFlushValue(h1) > straightFlushValue(h2)
		elif fourOfAKindValue(h1) != fourOfAKindValue(h2):
			return fourOfAKindValue(h1) > fourOfAKindValue(h2)
		elif fullHouseValue(h1) != fullHouseValue(h2):
			return fullHouseValue(h1) > fullHouseValue(h2)
		elif flush(h1) != flush(h2):
			return flush(h1)
		elif straightValue(h1) != straightValue(h2):
			return straightValue(h1) > straightValue(h2)
		elif threeOfAKindValue(h1) != threeOfAKindValue(h2):
			return threeOfAKindValue(h1) > threeOfAKindValue(h2)
		elif twoPairValue(h1) != twoPairValue(h2):
			return twoPairValue(h1) > twoPairValue(h2)
		elif onePairValue(h1) != onePairValue(h2):
			return onePairValue(h1) > onePairValue(h2)
	else:
		h1vals = sorted(handValues(h1))
		h2vals = sorted(handValues(h2))
		while len(h1vals) > 0:
			h1best = h1vals.pop()
			h2best = h2vals.pop()
			if h1best > h2best:
				return True
			elif h1best < h2best:
				return False
		'''
		while len(h1) > 0:
			if popHighCard(h1) > popHighCard(h2):
				print "p1 wins", h1, h2
				return True
			else:
				print "p2 wins", h1, h2
				return False
		return "same hand"
		'''


count = 0
while len(p1cards) > 0:
	p1hand = getHand(p1cards)
	p2hand = getHand(p2cards)
	if p1wins(p1hand,p2hand):
		count += 1

print count


# debug

h3 = ['TC','TC','TC','KC','KC']
h4 = ['TC','TC','TC','TC','AC']

print p1wins(h1, h2)