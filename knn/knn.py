from math import *
from pylab import *

def knn(point, data, k):
	# extract k-nearest neighbors
	neighbors = [[0, 0, 0, 10000] for x in range(k)]
	for cur in data:
		dist = math.sqrt((point[0] - cur[0])**2 + (point[1] - cur[1])**2)
		if neighbors[0][3] > dist:
			neighbors[0] = cur[:] + [dist]
			neighbors.sort(key = lambda arr : arr[3], reverse=True)
	
	# determine point class
	classes = {1 : 0, -1 : 0}
	for n in neighbors:
		classes[n[2]] += 1
	if classes[1] > classes[-1]: return 1  
	else: return -1

# knn usage
file = open('sample.dat')
dataset = []
for line in file:
	dataset.append([int(x) for x in line.split()])

x, y = [], []
for k in range(1, 20, 2):
	correct = 0
	result = []
	for cur in dataset:
		dt = dataset[:]
		dt.remove(cur)
		if knn(cur, dt, k) == cur[2]:
			correct += 1
			result.append(cur + [1])
		else:
			result.append(cur + [0])

	# plot classified results
	scatter([row[0] for row in result if row[2] == 1], [row[1] for row in result if row[2] == 1], c=[('b' if row[3] == 1 else 'r') for row in result if row[2] == 1], hold='on', s = 20)
	scatter([row[0] for row in result if row[2] == -1], [row[1] for row in result if row[2] == -1], c=[('b' if row[3] == 1 else 'r') for row in result if row[2] == -1], marker='^', s = 40)
	xlabel('classify with k = ' + str(k))
	show()
		
	x.append(k)
	y.append(correct)
	print k, correct

# plot correct classified samples on different k
plot(x, y)
xlabel('k parameter')
ylabel('correct classified samples')
show()