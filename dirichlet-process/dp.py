
# todo: email for multinomial distribution and effect of T on it, i think T damages the distribution

from math import *
import numpy as np

# laad data
file = open('students.dat')
data = []
for line in file:
	data.append(int(line))

# data
Y = np.array(data)
# labels
X = len(Y) * [Y.mean()]

# G0 ~ N(muG, sigmaG) # best guess of G
muG, sigmaG = Y.mean(), Y.std()
A0 = 0.01 # strength of belief that G0 is G

def makeClusters(): # make cluster dictionary from data and labels
	clusters = {}
	for i in range(len(Y)):
		if not clusters.has_key(X[i]): clusters[X[i]] = []
		clusters[X[i]].append(Y[i])
	return clusters

from scipy.stats import norm
def phi(d): # value of d in normal distribution function
	return norm.pdf(d)

def A(y):
	muF, sigmaF = 0, 1
	sigmaSum = sigmaF**2 + sigmaG**2
	return exp(-1 * (muF + muG)**2 / (2*sigmaSum)) / sqrt(2*pi*sigmaSum)

# mu0: mean of current cluster
def getLabelOfNewCluster(y, mu0):
	return np.random.normal((mu0 + y)/2, 2**-.5) # sample Gausian distribution

# iterations
for itr in range(1, 10):
	clusters = makeClusters()

	# update X[i] in n+1 way using the multinomial selector
	for i in range(len(Y)):
		probabilites = [] # of each condition
		for label, items in clusters.iteritems():
			probabilites.append(phi(Y[i] - label))
		probabilites.append(A(Y[i]))
		probabilites = np.array(probabilites)

		# sum of probabilites equals to 1
		probabilites /= probabilites.sum()
		
		# sample from multinomial distribution
		choice = np.random.multinomial(1, probabilites).tolist().index(1) # search the 1 element's index

		if choice == len(clusters): # add new cluster
			X[i] = getLabelOfNewCluster(Y[i], np.array(clusters[X[i]]).mean())
			clusters = makeClusters()
		else: # change cluster
			X[i] = clusters.keys()[choice]

	# print results
	clusters = makeClusters()
	print '\n'
	for label, items in clusters.iteritems():
		print '{:.2f} -> {}'.format(label, items)
	print 'iteration: {}, clusters: {}'.format(itr, len(clusters))
