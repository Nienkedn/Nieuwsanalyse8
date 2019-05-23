import csv
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt


def get_sub_pol_array():
    x = []
    y = []
    c = []

    with open('../Data/data2.csv', 'r') as csv_file:
        reader = csv.reader((l.replace('\0', '') for l in csv_file))
        next(reader)

        for i in reader:
            if i:
                x.append([float(i[6])])
                y.append([float(i[7])])
                c.append([float(i[6]), float(i[7])])

        return x, y, c


def scatter_result():
    result = get_sub_pol_array()
    plt.scatter(result[0], result[1])
    plt.show()


def cluster_transform():
    result = get_sub_pol_array()
    colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k']
    cluster_amount = 3

    kmeans = KMeans(n_clusters=cluster_amount)
    kmeansoutput = kmeans.fit_predict(result[2])
    print(kmeansoutput)

    for i, x in enumerate(kmeansoutput):
        result[2][i].append(x)

    pca = PCA(n_components=2).fit(result[2])
    pca_d = pca.transform(result[0])
    pca_c = pca.transform(result[1])

    for i, x in enumerate(result[2]):
        for k in range(0, cluster_amount):
            if x[2] == k:
                plt.scatter(pca_d[i][0], pca_c[i][1], c=colors[k], s=10, alpha=0.5)

    plt.show()


def cluster_no_transform():
    result = get_sub_pol_array()
    colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k']
    cluster_amount = 3

    kmeans = KMeans(n_clusters=cluster_amount)
    kmeansoutput = kmeans.fit_predict(result[2])
    print(kmeansoutput)

    for i, x in enumerate(kmeansoutput):
        result[2][i].append(x)

    for i, x in enumerate(result[2]):
        for k in range(0, cluster_amount):
            if x[2] == k:
                plt.scatter(result[2][i][0], result[2][i][1], c=colors[k], s=10, alpha=0.5)

    plt.show()


if __name__ == "__main__":
    cluster_no_transform()
