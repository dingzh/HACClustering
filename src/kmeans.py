from __future__ import print_function
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

#get sentences
corpus = open('../coreNLP/demo.out','r')
sents = corpus.readlines()
corpus.close()

#vectorize
bigram_vectorizer = CountVectorizer(ngram_range=(2, 2),token_pattern=r'\b\w+\b',
									min_df=1, stop_words='english')
data = bigram_vectorizer.fit_transform(sents)

#clustering
true_k = 10
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=9999, n_init=1)
model.fit(data)

#output result
#print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = bigram_vectorizer.get_feature_names()
for i in range(true_k):
    print("")
    for ind in order_centroids[i, :-1]:
        print(terms[ind],end=',')
