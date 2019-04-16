import csv
import xml.etree.ElementTree as ET
import collections
import numpy as np
import matplotlib.pyplot as plt


def sentiment_word_count():
    with open('../Data/tweets.csv', 'r', newline='') as csv_file:
        # De 'reader' variabele bevat alle rijen uit het csv bestand en filtert alle cellen met NULL waarde eruit.
        reader = csv.DictReader((l.replace('\0', '') for l in csv_file))
        rows = list(reader)
        tree = ET.parse('../Data/nl-sentiment.xml')
        words = tree.findall('.//word')

        bad_characters = ['.', ':', '!', '?']
        found_words = []
        for word in words:
            word = word.get('form').lower()
            for tweet in rows:
                tweet = tweet['Content']
                for char in bad_characters:
                    tweet = tweet.replace(char, '')
                tweet_words = tweet.split(" ")
                for tweet_word in tweet_words:
                    if tweet_word.lower() == word:
                        found_words.append(word)

    counter = collections.Counter(found_words)
    label = list(map(lambda x: x[0], counter.most_common(15)))
    number = list(map(lambda x: x[1], counter.most_common(15)))

    index = np.arange(len(label))
    plt.bar(index, number)
    plt.xlabel('Words', fontsize=15)
    plt.ylabel('Number of references', fontsize=15)
    plt.xticks(index, label, fontsize=15, rotation=30)
    plt.title('Most common words in dataset')
    plt.show()


def time_word_count():
    with open('../Data/tweets.csv', 'r', newline='') as csv_file:
        # De 'reader' variabele bevat alle rijen uit het csv bestand en filtert alle cellen met NULL waarde eruit.
        reader = csv.DictReader((l.replace('\0', '') for l in csv_file))
        rows = list(reader)
        tree = ET.parse('../Data/nl-sentiment.xml')
        words = tree.findall('.//word')

        bad_characters = ['.', ':', '!', '?']
        found_words = []
        for word in words:
            word = word.get('form').lower()
            for tweet in rows:
                tweet = tweet['Content']
                for char in bad_characters:
                    tweet = tweet.replace(char, '')
                tweet_words = tweet.split(" ")
                for tweet_word in tweet_words:
                    if tweet_word.lower() == word:
                        found_words.append(word)

    counter = collections.Counter(found_words)
    label = list(map(lambda x: x[0], counter.most_common(15)))
    number = list(map(lambda x: x[1], counter.most_common(15)))

    index = np.arange(len(label))
    plt.bar(index, number)
    plt.xlabel('Words', fontsize=15)
    plt.ylabel('Number of references', fontsize=15)
    plt.xticks(index, label, fontsize=15, rotation=30)
    plt.title('Most common words in dataset')
    plt.show()


time_word_count()
