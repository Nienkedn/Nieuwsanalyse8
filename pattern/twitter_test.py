from pattern.web import Twitter, plaintext
from pattern.text.en import tag
from pattern.text.nl import sentiment as sentiment_nl
from pattern.vector import KNN, count
import csv


def proefje():
    twitter, knn = Twitter(), KNN()
    for i in range(1, 10):
        for tweet in twitter.search('#win OR #fail', start=i, count=100):
            s = tweet.text.lower()
    p = '#win' in s and 'WIN' or 'FAIL'
    v = tag(s)
    v = [word for word, pos in v if pos == 'JJ']  # JJ = adjective
    v = count(v)
    if v:
        knn.train(v, type=p)

    print(knn.classify('sweet potato burger'))
    print(knn.classify('stupid autocorrect'))


def proefje2():
    x = []
    for tweet in Twitter().search("windmolens", count=100):
        if tweet.language in "nl":
            s = plaintext(tweet.description)
            w = sentiment_nl(s)
            print(s)
            print(w)
            print('-----------------------------------------------------')
            x.append(w)
            print(len(x))

    print(x)


def eigen_data():
    newRows = []

    with open('data/data.csv', 'r') as csv_file:
        reader = csv.reader((l.replace('\0', '') for l in csv_file))

        for row in reader:
            if row and row[0].startswith('ÿþOrigin'):
                row[0] = 'Origin'
                row.append('Polarity')
                row.append('Subjectivity')
                newRows.append(row)
            elif row:
                s = plaintext(row[2])
                w = sentiment_nl(s)
                row.append(w[0])
                row.append(w[1])
                newRows.append(row)

    with open('data/data2.csv', 'w', newline='', encoding='utf-16') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        writer.writerows(newRows)


if __name__ == "__main__":
    eigen_data()
