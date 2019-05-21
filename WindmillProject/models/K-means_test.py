from sklearn.feature_extraction.text import TfidfVectorizer
from stop_words import get_stop_words
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import adjusted_rand_score

omroepzeeland = open("../Data/omroep_zeeland.csv", mode="r", encoding="utf-16")
nu = open("../Data/data.csv", mode="r", encoding="utf-16")
tweets = open("../Data/tweets.csv", mode="r", encoding="utf-16")

stop_words = get_stop_words('dutch')
vectorizer = TfidfVectorizer(stop_words)
X = vectorizer.fit_transform(omroepzeeland)
terms = vectorizer.get_feature_names()

true_k = 4
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

terms_vectorized = vectorizer.transform(terms)
terms_prediction = model.predict(terms_vectorized)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
# terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print

print("\n")
print("Prediction")

print("\n")
# print(order_centroids)
plt.show()
