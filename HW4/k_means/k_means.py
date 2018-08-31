import numpy as np
from pyspark import SparkConf, SparkContext


def kmeans(data, centroid):
    max_iter = 100
    conf = SparkConf()
    sc = SparkContext(conf=conf)
    data = sc.textFile(data).map(lambda l: np.array([float(i) for i in l.split(' ')])).cache()
    centroid = sc.textFile(centroid).map(lambda l: np.array([float(i) for i in l.split(' ')])).collect()
    for i in range(max_iter):
        temp_data = data.map(lambda x: (np.argmin([np.linalg.norm(x - s) for s in centroid]), (x, 1)))
        temp_centroid = temp_data.reduceByKey(lambda x1, x2: (x1[0] + x2[0], x1[1] + x2[1])).sortByKey()
        centroid = np.array(temp_centroid.map(lambda x: x[1][0] / x[1][1]).collect())
    file = open("results.txt", "w")
    for c in centroid:
        line = ""
        for item in c:
            line += str(item) + " "
        file.write(line + "\n")
    file.close()


if __name__ == '__main__':
    kmeans('data.txt', 'c1.txt')
