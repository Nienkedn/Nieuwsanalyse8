from sklearn.feature_extraction.text import TfidfVectorizer
from stop_words import get_stop_words
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import adjusted_rand_score
from collections import Counter

# These are the csv files, we are going to use for our script
omroepzeeland = open("../Data/omroep_zeeland.csv", mode="r", encoding="utf-16")
nu = list(open("../Data/nu_nl.csv", mode="r", encoding="utf-16"))[1:]
tweets = open("../Data/tweets.csv", mode="r", encoding="utf-16")

# The csv files will be passed through and if the texts contains stopwords, all of them will be removed from the resulting tokens. It will be converted to a matrix of TF-IDF features.
stop_words = get_stop_words('dutch')
my_stop_words = (["null", "http", "bit", "www", "https", "html", "ly", "nl", "com", "origin", "Timestamp", "Content", "Title", "Comment_count", "Retweet_count", "twitter", "000", "10", "11", "12", "13",
                  "14", "17", "rtvu"])
vectorizer = TfidfVectorizer(stop_words = stop_words + my_stop_words)

# X = vectorizer.fit_transform(omroepzeeland)
Y = vectorizer.fit_transform(nu)
# Z = vectorizer.fit_transform(tweets)
terms = vectorizer.get_feature_names()

# Clusters the data in groups of equal variance, minimizing a criterion known as the inertia or within-cluster sum-of-squares
true_k = 5
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=1000, n_init=10, random_state=5)
# model.fit(X)
model.fit(Y)
# model.fit(Z)

# Print the results
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
for i in range(true_k):
   print("\n""Cluster %d:" % i),
   for ind in order_centroids[i, :10]:
       print(' %s' % terms[ind]),

# Explanation of the model, script en TFIDF
# We hebben zo ingesteld dat er uit de drie bronnen(nu.nl, twitter en omroepzeeland) vijf clusters gemaakt moeten worden. Eerst worden uit de drie bronnen de stopwoorden eruit gefilterd. Daarna word er door
# middel van term frequency-inverse document frequency aka TFIDF aan ieder woord een cijfer gegeven om zo aan te geven hoe belangrijk het woord is voor de tekst. Deze informatie wordt door het K-means algoritme
# gebruikt om de belangrijkste woorden te groeperen in clusters. Hierbij staan de belangrijkste woorden in cluster 1 en de minder belangrijke woorden in het laatste cluster

print(Y)
print(vectorizer.get_feature_names())
# print(pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names()))
# Mee bezig, zie http://jonathansoma.com/lede/foundations/classes/text%20processing/tf-idf/

word1 = 'windmolens'
word2 = 'energie'
xdata = model.cluster_centers_[:,vectorizer.vocabulary_[word1]]
ydata = model.cluster_centers_[:,vectorizer.vocabulary_[word2]]

plt.scatter(xdata, ydata, s=1)
for clusternum, (xcoord,ycoord) in enumerate(zip(xdata, ydata)):
    plt.text(xcoord, ycoord, str(clusternum))
plt.title('TFIDF score in cluster')
plt.xlabel(word1)
plt.ylabel(word2)
plt.show()

print(Counter(model.labels_))
nu1 = [text for clusternum, text in zip(model.labels_,nu) if clusternum == 3]
print(nu1)

# regex bij token pattern
# woordcloud maken van die woorden en selecteren van onderscheidende woorden
