from math import *

data = [
	['A', 'D', 'E'],
	['A', 'B', 'C', 'E'],
	['A', 'B', 'D', 'E'],
	['A', 'C', 'D', 'E'],
	['B', 'C', 'E'],
	['B', 'D', 'E'],
	['C', 'D'],
	['A', 'B', 'C'],
	['A', 'D', 'E'],
	['A', 'B', 'E']
]

# data = [
# 	['A', 'D', 'E'] + ['A', 'B', 'C', 'E'],
# 	['A', 'B', 'D', 'E'] + ['A', 'C', 'D', 'E'],
# 	['B', 'C', 'E'] + ['B', 'D', 'E'],
# 	['C', 'D'] + ['A', 'B', 'C'],
# 	['A', 'D', 'E'] + ['A', 'B', 'E']
# ]

def filterData(items, d):
	return filter(lambda basket: [val for val in items if val in basket] == items, d)

# [val for val in items if val in basket] = intersecion of items and basket
def support(items):
	return len(filterData(items, data)) / float(len(data))

def confidence(X, Y): # X => Y rule
	return support(X + Y) / support(X)

def P(X, Y = []):
	return support(X + Y)

def PCond(Y, X): # P(Y|X)
	fd = filterData(X, data)
	return float(len(filterData(Y, fd))) / len(fd)

def PS(X, Y):
	return P(X, Y) - P(X) * P(Y)

def Lift(X, Y):
	return PCond(Y, X) / P(Y)

def phiCoeff(X, Y):
	return PS(X, Y) / sqrt(P(X)*(1 - P(X)) * P(Y)*(1 - P(Y)))

def OddsRatio(X, Y):
	return P(X, Y) * P(Xn, Yn) / (P(Xn, Y) * P(X, Yn))

# print support(['E']), support(['B', 'D']), support(['B', 'D', 'E'])

x, y = ['B', 'D'], ['E']

print confidence(x, y), confidence(y, x)
print PS(x, y), PS(y, x)
print Lift(x, y), Lift(y, x)
print  phiCoeff(x, y), phiCoeff(y, x)

def charRule(items):
	print items
	for item in items:
		titems = items[:]
		titems.remove(item)
		# print '{:.2f}'.format(confidence([item], titems))
		print '{:.2f}'.format(confidence(titems, [item]))

charRule(['A', 'B', 'C'])
charRule(['A', 'B'])

file = open('out.txt')
nodes = []
for line in file:
	nodes.append(line.strip())

for i in range(7):
	row = filter(lambda node: len(node.split()) == i, nodes)
	for node in row:
		sup = int(node.split()[-1:][0][1:-1]) # inside () of the last item
		if sup < 30: label = 'I'
		else: label = 'F'
		print "'{} :{}',".format(node, label),
	print
		

Exercise Cholesterol Smoking Retired Sup_Count
data = \
	[['Exercise=Yes', 'Cholesterol=High', 'Smoking=Yes', 'Retired=Yes']] * 2 + \
	[['Exercise=Yes', 'Cholesterol=High', 'Smoking=Yes', 'Retired=No',]] *42 + \
	[['Exercise=Yes', 'Cholesterol=High', 'Smoking=No', 'Retired=Yes']] * 0 + \
	[['Exercise=Yes', 'Cholesterol=High', 'Smoking=No', 'Retired=No',]] *14 + \
	[['Exercise=Yes', 'Cholesterol=Low', 'Smoking=Yes', 'Retired=Yes']] * 2 + \
	[['Exercise=Yes', 'Cholesterol=Low', 'Smoking=Yes', 'Retired=No']] * 8 + \
	[['Exercise=Yes', 'Cholesterol=Low', 'Smoking=No', 'Retired=Yes']] * 6 + \
	[['Exercise=Yes', 'Cholesterol=Low', 'Smoking=No', 'Retired=No',]] *16 + \
	[['Exercise=No', 'Cholesterol=High', 'Smoking=Yes', 'Retired=Yes',]] *42 + \
	[['Exercise=No', 'Cholesterol=High', 'Smoking=Yes', 'Retired=No',]] *10 + \
	[['Exercise=No', 'Cholesterol=High', 'Smoking=No', 'Retired=Yes',]] *12 + \
	[['Exercise=No', 'Cholesterol=High', 'Smoking=No', 'Retired=No']] * 6 + \
	[['Exercise=No', 'Cholesterol=Low', 'Smoking=Yes', 'Retired=Yes',]] *12 + \
	[['Exercise=No', 'Cholesterol=Low', 'Smoking=Yes', 'Retired=No']] * 1 + \
	[['Exercise=No', 'Cholesterol=Low', 'Smoking=No', 'Retired=Yes',]] *24 + \
	[['Exercise=No', 'Cholesterol=Low', 'Smoking=No', 'Retired=No']] * 3 


# print data

data = filter(lambda basket: 'Retired=Yes' in basket , data)

print support(['Exercise=Yes', 'Cholesterol=Low']), confidence(['Exercise=Yes'], ['Cholesterol=Low'])
print support(['Exercise=No', 'Cholesterol=Low']), confidence(['Exercise=No'], ['Cholesterol=Low'])


# TID Temperature Pressure Alarm_1 Alarm_2 Alarm_3
data = [
	[1, 95, 1105, 0, 0, 1],
	[2, 85, 1040, 1, 1, 0],
	[3, 103, 1090, 1, 1, 1],
	[4, 97, 1084, 1, 0, 0],
	[5, 80, 1038, 0, 1, 1],
	[6, 100, 1080, 1, 1, 0],
	[7, 83, 1025, 1, 0, 1],
	[8, 86, 1030, 1, 0, 0],
	[9, 101, 1100, 1, 1, 1],
]

