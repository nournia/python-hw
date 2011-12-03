from pylab import *

# data
data = [
	[1, 0.73, 0.61],
	[1, 0.69, 0.03],
	[0, 0.44, 0.68],
	[0, 0.55, 0.31],
	[1, 0.67, 0.45],
	[1, 0.47, 0.09],
	[0, 0.08, 0.38],
	[0, 0.15, 0.05],
	[1, 0.45, 0.01],
	[0, 0.35, 0.04]
]

fpr, tpr = [0], [0]

for bond in [x * 0.1 for x in range(0, 11)]:

	# two classifier
	for m in [1, 2]:

		fpr.append([])
		tpr.append([])
		TP, FP, FN, TN = 0, 0, 0, 0

		for d in data:
			cl = 1 if  d[m] > bond else 0
	
			if m == 2:
				cl = 1 if  d[m] <= bond else 0
	
			if cl == 1:
				if cl == d[0]: TP += 1 
				else: FP += 1
			else:
				if cl == d[0]: TN += 1 
				else: FN += 1

		# precision = float(TP) / (TP + FP)
		# recall = float(TP) / (TP + FN)
		# F = 2 * (precision * recall) / (precision + recall)

		fpr[m] += [float(FP) / (FP + TN)]
		tpr[m] += [float(TP) / (TP + FN)]

# TPR - y, FPR - x
plot(tpr[1], fpr[1])
plot(tpr[2], fpr[2])
show()