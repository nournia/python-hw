from data import *

import numpy as np
import pylab as pl
from sklearn import linear_model


""" homes: linear """
clf = linear_model.LinearRegression()
pl.scatter(homes[:, 0], homes[:, 1])

# linear regression
clf.fit([[x] for x in homes[:, 0]], homes[:, 1]) # X, y

def func(x):
	return clf.coef_ * x + clf.intercept_
pl.plot([1, 6000], [func(1), func(6000)])

pl.plot([2000, 1500], [clf.predict([2000]), clf.predict([1500])], 'ro')

pl.show()


""" scores: linear """
clf = linear_model.LinearRegression()
clf.fit([[p1] for p1 in scores[:, 1]], scores[:, 0]) # P1, F
print 'B0 = {:.2f}, B1 = {:.2f}, Residues = {:.2f}'.format(clf.intercept_, clf.coef_[0], clf.residues_[0])

clf.fit([[p2] for p2 in scores[:, 2]], scores[:, 0]) # P2, F
print 'B0 = {:.2f}, B2 = {:.2f}, Residues = {:.2f}'.format(clf.intercept_, clf.coef_[0], clf.residues_[0])

clf.fit(scores[:, 1:], scores[:, 0]) # P1, P2, F
print 'B0 = {:.2f}, B1 = {:.2f}, B2 = {:.2f}, Residues = {:.2f}'.format(clf.intercept_, clf.coef_[0], clf.coef_[1], clf.residues_[0])
print clf.predict([78, 85])

""" rivers: linear """
clf = linear_model.LinearRegression()
for i in range(1, 5):
	pl.subplot(2, 2, i)
	pl.scatter(rivers[:, i], rivers[:, 0])
	
	X = [[x] for x in  rivers[:, i]]
	clf.fit(X, rivers[:, 0])
	pl.plot(X, clf.predict(X))
	pl.xlabel('feature: X{}'.format(i))

pl.show()


""" factories: logestic regression """
def prec(mask):
	return float(mask.sum()) / len(mask)

clf = linear_model.LogisticRegression()
for i in range(1, 4):
	pl.subplot(2, 2, i)
	pl.scatter(factories[:, i], factories[:, 0])

	X = [[x] for x in  factories[:, i]]
	clf.fit(X, factories[:, 0])

	print prec(factories[:, 0] == clf.predict(X))

	mask = (factories[:, 0] != clf.predict(X))
	pl.plot(factories[:, i][mask], factories[:, 0][mask], 'ro')
	pl.xlabel('feature: X{}'.format(i))

pl.show()

X = factories[:, 1:4]
y = factories[:, 0]
clf.fit(X, y)
print prec(clf.predict(X) == y)


""" cars: linear, ridge, lasso"""
def error(a, b):
	return ((a - b)**2).sum() / len(a);

X, y = cars[:, 1:12], cars[:, 0]

clf = linear_model.LinearRegression()
clf.fit(X, y)
print error(clf.predict(X), y)

clf = linear_model.Ridge(alpha = .5)
clf.fit(X, y)
print error(clf.predict(X), y)

clf = linear_model.Lasso(alpha = .1)
clf.fit(X, y)
print error(clf.predict(X), y)
