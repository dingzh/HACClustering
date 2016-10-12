from __future__ import print_function
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import AgglomerativeClustering
import sys

#get sentences
sents = []
maxlen = 200
with open('/home/dean/coreNLP/demo.out','r') as corpus:
	for line in corpus.readlines():
		if len(line) < maxlen:
			sents.append(line)
size = len(sents)

#vectorize
bigram_vectorizer = CountVectorizer(ngram_range=(2, 2),token_pattern=r'\b[\d( \.)]+|\w+\b',min_df=1)
data = bigram_vectorizer.fit_transform(sents)
dataarray = data.toarray()
print('size of data for clustering: ', len(dataarray))
#print('length of vector', len(dataarray[1]))

#clustering
true_n = int(sys.argv[1])
clustering = AgglomerativeClustering(n_clusters = true_n)
clustering.fit(dataarray)

#output result

labels = clustering.labels_
res = list()
#init list to store res
for i in range(true_n):
	res.append(list())
for i in range(size):
	res[labels[i]].append(sents[i])
#write to file
for i in range(true_n):
	print("Cluster {}:".format(i))
	for line in res[i]:
		print(line, end='')
		



