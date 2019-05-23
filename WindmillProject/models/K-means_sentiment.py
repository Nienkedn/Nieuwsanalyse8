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


def cluster_results():
    result = get_sub_pol_array()

    pca = PCA(n_components=1).fit(result[1])
    pca_d = pca.transform(result[1])
    pca_c = pca.transform(result[0])

    kmeans = KMeans(n_clusters=4)
    kmeansoutput = kmeans.fit(result[1])

    plt.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)
    # plt.show()
    #
    # clusters = KMeans(n_clusters=4, random_state=5).fit(result[2])
    # c2 = clusters.transform(result[2])
    # centroids = clusters.cluster_centers_
    #
    #
    # plt.scatter(c2[0], c2[1], c='r', s=10, alpha=0.5)
    # plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
    #
    # plt.scatter(result[0], result[1], c='red', s=50)
    plt.show()


if __name__ == "__main__":
    cluster_results()
