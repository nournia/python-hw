import numpy as np
import pylab as pl
from sklearn import svm, cross_validation

file = open('sample.dat')
X, y = [], []
for line in file:
	row = [int(x) for x in line.split()]
	X.append(row[:2])
	y.append(row[2])
X, y = np.array(X), np.array(y)

def printConfusion(confusion):
	[TP, FP, TN, FN] = confusion

	print 'precision = %.2f' % (float(TP) / (TP + FP))
	print 'recall = %.2f' % (float(TP) / (TP + FN))
	print 'confusion matrix:'
	print '	N	P'
	print 'N	%d	%d' % (TN, FP)
	print 'P	%d	%d' % (FN, TP)
	print

def getConfusion(Y, Z):
	TP, FP, TN, FN = 0, 0, 0, 0
	for y, z in zip(Y, Z):
		if z > 0:
			if y > 0: TP += 1
			else: FP += 1
		else:
			if y < 0: TN += 1
			else: FN += 1
	return np.array([TP, FP, TN, FN])

iterations = 1
ss = cross_validation.ShuffleSplit(len(y), n_iterations=iterations, test_fraction=0.1, random_state=10)

predicts, ensemble = [], []
for clf in [svm.SVC(kernel='linear', C=5), svm.SVC(kernel='poly', gamma=0.01, degree=3), svm.SVC(kernel='rbf', gamma=.002)]:
	print clf
	confusion = np.array([0., 0., 0., 0.])
	supports = 0
	for train, test in ss:
		clf.fit(X[train], y[train])
		confusion += getConfusion(y[test], clf.predict(X[test]))
		supports += len(clf.support_)

		if len(predicts) == 0:  predicts = clf.predict(X[test])
		else: predicts += clf.predict(X[test])
		ensemble = getConfusion(y[test], predicts)

	confusion /= iterations
	supports /= iterations
	print 'support vectors = %d' % supports
	printConfusion(confusion)

print 'ensemble: '
printConfusion(ensemble)
