def stripResults(filename):
	file = open(filename)
	row = 'query, training, validation, test'
	for line in file:
		if line.startswith('query:'):
			print row
			row = line.split(':')[1].strip()

		if line.startswith('NDCG@10 on training data:') or line.startswith('NDCG@10 on validation data:') or  line.startswith('NDCG@10 on test data:'):
			row += ',' + line.split(':')[1].strip()
	print row

import numpy as np
def show(filename):
	data = []
	file = open(filename)
	for line in file:
		data.append([float(x) for x in line.split(',')[1:]])
	data = np.array(data)
	
	for i in range(3):
		print '{:.2f}'.format(data[:, i].mean()),
	print 

# stripResults('resources/RankLib-vv1.1/results/AllKernelPCAed')

print 'type, training, validation, test'
for name in ['rankboost', 'pca', 'kernelpca', 'allrankboost', 'allpca', 'allkernelpca', ]:
	print name, 
	show('resources/RankLib-v1.1/results/'+ name)