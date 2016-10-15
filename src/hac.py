from __future__ import print_function
from sklearn.feature_extraction import DictVectorizer
from sklearn.cluster import AgglomerativeClustering
import sys
from simhash import Simhash 
from readCurrency import currencies
import re

def convert2Dict(s):
	featureDict = dict()
	for i in range(64):
		featureDict[i] = s[i]
	return featureDict

def getFeatures(s):
    width = 3
    s = s.lower()
    for curr in currencies:
    	s = s.replace(curr, 'currency')
    s = re.sub(r'[^\w]+', '', s)
    s = re.sub(r'\d+', '', s)
   	# print(s)
    return [s[i:i+width] for i in range(max(len(s) - width + 1, 1))]

print(sys.argv)
#get sentences; handle sents with nums first, more likely to gut clusters
sents = []
maxlen = 200
numRe = re.compile(r'\d+')
with open('/home/dean/coreNLP/demo.out','r') as corpus:
	for line in corpus.readlines():
		if len(line) > maxlen:
		 	line = line[:90] + '\n'
		res = numRe.search(line)
		if res is not None:
			sents.append(line)
size = len(sents)
print('Num of sentences for clustering: ', size)

#vectorize with simhash 
hashList = ['{0:064b}'.format(Simhash(getFeatures(sent)).value) for sent in sents]
featureDictList = [convert2Dict(x) for x in hashList]

vectorizer = DictVectorizer()
data = vectorizer.fit_transform(featureDictList)
dataarray = data.toarray()

#clustering
# true_n = 5
true_n = int(sys.argv[1])
#use manhattan 
clustering = AgglomerativeClustering(n_clusters = true_n)
#	affinity = 'hamming', linkage = 'complete', connectivity = None)
clustering.fit(dataarray)

#output result

labels = clustering.labels_
res = list()
#init list to store res
for i in range(true_n):
	res.append(list())
for i in range(size):
	res[labels[i]].append(sents[i])

#print, big size first
printOrder = list()
for x in res:
	printOrder.append((len(x),x))
printOrder.sort(reverse=True)
clusteri = 0
for x, cluster in printOrder:
	print("Cluster:{} size {}".format(clusteri,x))
	clusteri += 1
	for line in cluster:
		if len(line) > 160:
			print('\t',line[:160])
		else:
			print('\t',line,end='')
	print('')	



