from math import *
import numpy as np

# dendrogram
import hcluster
similarity = [
	[1.00, 0.93, 0.86, 0.84, 0.69, 0.65],
	[0.93, 1.00, 0.79, 0.83, 0.64, 0.67],
	[0.86, 0.79, 1.00, 0.75, 0.82, 0.54],
	[0.84, 0.83, 0.75, 1.00, 0.57, 0.79],
	[0.69, 0.64, 0.82, 0.57, 1.00, 0.36],
	[0.65, 0.67, 0.54, 0.79, 0.36, 1.00],
]

Z = hcluster.single(similarity)
hcluster.dendrogram(Z)

# k-means
data = np.array([6, 12, 18, 24, 30, 42, 48])

centroids = np.array([18, 45])
# centroids = np.array([15, 40])

def dist(x, y): return abs(x - y)

clusters = {}
for center in centroids:
	clusters[center] = []

for point in data:
	index = centroids[abs(point - centroids).argmin()]
	clusters[index] += [point]

for center, cluster in clusters.items():
	cluster = np.array(cluster)
	print '{}: {}, SSE = {}, mean = {}'.format(center, cluster, ((cluster - center)**2).sum(), cluster.mean())

# labels = [1, 1, 2, 2]
# incidence = np.array([
# 	[1, 1, 0, 0],
# 	[1, 1, 0, 0],
# 	[0, 0, 1, 1],
# 	[0, 0, 1, 1],
# ])
# proximity = np.array([
# 	[1, 0.9, 0.35, 0.45],
# 	[0.9, 1, 0.3, 0.4],
# 	[0.35, 0.3, 1, 0.7],
# 	[0.45, 0.4, 0.7, 1],
# ])

# entropy, purity
clusters = np.array([
	[2, 1, 2, 123, 4],
	[13, 120, 3, 6, 4],
	[132, 14, 5, 2, 2],
	[19, 7, 73, 11, 8],
	[5, 12, 6, 4, 112],
])

entropy, purity = [], []
for cluster in clusters:
	cluster = np.array(cluster)
	cluster = cluster / float(cluster.sum())

	e = (cluster * [log(x, 2) for x in cluster]).sum()
	p = cluster.max()
	entropy += [e]
	purity	+= [p]

counts = np.array([c.sum() for c in clusters])
coeffs = counts / float(counts.sum())
print 'entropy: ', (coeffs * entropy).sum()
print 'purity: ', (coeffs * purity).sum()