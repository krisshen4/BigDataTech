import numpy as np
import sys
import re
import pyspark

def nearest_center(data_point, center):
    """
    Find the nearest center
    :param data_point: data point
    :param center:  data of centroid
    :return: (cluster center, data point)
    """
    min_dist = float(np.Inf)
    min_dist_index = 0
    for i in range(len(center)):
        dist = np.linalg.norm(data_point - center[i][0])
        if dist < min_dist:
            min_dist = dist
            min_dist_index = i
    return (min_dist_index, data_point)


def equal(rdd1, rdd2):
    """
    Check if rdd1 equals rdd2.
    :param rdd1: one iteration before centroids RDD
    :param rdd2: current centroids RDD
    :return: True if two RDDs have same centroid; False if not.
    """
    rdd1 = rdd1.map(lambda r: r[0]).collect()
    rdd2 = rdd2.map(lambda r: r[0]).collect()
    for i in rdd1:
        check = False
        for j in rdd2:
            if (i == j).all():
                check = True
                break
        if check == False:
            return False
    return True


def k_means(file_data, file_centroid):
    """
    K means algorithm application
    :param file_data: .txt file containing all data point
    :param file_centroid: .txt file containing all initial centroid points
    :return: RDD object containing final centroid points after k means process
    """
    data = sc.testFile(file_data).map(lambda line: np.array([float(x) for x in line.split("")])).cache()
    centroid = sc.testFile(file_centroid).map(lambda line: np.array([float(x) for x in line.split("")])).cache()
    centroid = centroid.zipWithIndex().collect()

    iter = 0
    while (iter < 20):
        group = data.map(lambda data_point: nearest_center(data_point, centroid))
        group = group.groupByKey().map(lambda x: (x[0], list(x[1])))
        centroid_update = group.map(lambda x: (np.mean(x[1], axis=0), x[0]))
        centroid_update = centroid_update.collect()
        if equal(centroid, centroid_update):
            print(iter)
            break
        iter +=1
    return centroid_update.map(lambda x: x[0])

if __name__ == "__main__":
    sc = pyspark.SparkContext(appName="kmeans")
    k_means(sys.argv[1], sys.argv[2])

