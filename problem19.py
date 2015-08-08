class Weekday():
	def __init__(self):
		self.i = 0 # monday = 0, so start at tuesday jan 1 1901
	def inc(self):
		self.i += 1
		if self.i > 6:
			self.i = 0
		return self.i

months = [
	31,
	28,
	31,
	30,
	31,
	30,
	31,
	31,
	31,
	30,
	30,
	31,
]

sundays = 0

week = Weekday()
for y in range(1901, 2001):
	leap = False
	if y % 4 == 0:
		leap = True
		if y % 100 == 0:
			leap = False
		if y % 400 == 0:
			leap = True
	if leap:
		months[1] = 29
	else:
		months[1] = 28
	for m in range(len(months)):
		for d in range(months[m]):
			dayOfWeek = week.inc()
			if d == 0:
				if dayOfWeek == 6:
					print (d,m,y)
					sundays += 1

print(sundays)
