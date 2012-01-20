import os
import numpy as np
import pylab as pl
from sklearn.decomposition import PCA, KernelPCA

folder = ''
def fileAddress(title):
	return folder + title +'.txt'

data, y, qid = [], [], []

def loadFile(kind, q = None):
	global data, y, qid
	data, y, qid = [], [], []

	file = open(fileAddress(kind))
	for line in file:
		# apply condition
		if q != None and not('qid:{}'.format(q) in line): continue

		# process line
		features = []
		first = True
		for word in line.split():
			if first:
				y.append(int(word))
				first = False
			elif word.startswith('qid'):
				qid.append(int(word.split(':')[1]))
			elif word.startswith('#'):
				break
			else:
				features.append(float(word.split(':')[1]))
		data.append(features)

def printFile(filename):

	def letorFormat(arr):
		tmp = ''
		for i in range(len(arr)):
			tmp += '{}:{} '.format(i+1, arr[i])
		return tmp

	file = open(fileAddress(filename), 'w')
	for i in range(0, len(y)):
		file.write('{} qid:{} {}\n'.format(y[i], qid[i], letorFormat(data[i])))
	file.close()

def doKernelPCA(q, components=40):
	global data

	# load test query
	loadFile('test', q)
	
	# fit model
	kpca = KernelPCA(components, kernel="rbf")
	kpca.fit(data)

	# transform and print test query
	data = kpca.transform(data)
	printFile('test{}'.format(q))

	for kind in ['train', 'vali']:
		loadFile(kind)
		data = kpca.transform(data)
		printFile(kind + str(q))
		
def doRankBoost(q = ''):
	rounds, metric = '1', 'NDCG@10'
	cmd = "java -jar resources/RankLib-v1.1/bin/RankLib.jar -train "+ fileAddress('train{}'.format(q)) +" -test "+  fileAddress('test{}'.format(q)) +" -ranker 2 -round "+ rounds +" -metric2t "+ metric +" -metric2T "+ metric  +" -validate "+ fileAddress('vali{}'.format(q))
	os.system(cmd)

for i in range(5):
	folder = 'resources/RankLib-v1.1/OHSUMED/QueryLevelNorm/Fold{}/'.format(i+1)
	
	# load test qids
	loadFile('test')
	qids = set(qid[:])

	for q in qids:
		print 'query: {}'.format(q)
		doKernelPCA(q, 10)
		doRankBoost(q)
