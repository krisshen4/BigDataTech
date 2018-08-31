import pyspark
import sys
import numpy as np

def add_v(x):
    """
    Add index to v
    :param x: a vector
    :return: a tuple containing index and value
    """
    for i in range(len(x)):
        yield(i, x[i])


def add_j(x):
    """
    Add j to (j, (i, val)) tuple
    :param x: a matrix
    :return: a tuple containing index and value
    """
    for i in x[1]:
        yield(i[1], (x[0], i[0]))


def matrix_multiply(file_A, file_v):
    """
    Multiply a matrix and a vector
    :param A: .txt file of a matrix
    :param v: .txt file of a vector
    :return: .txt file of the multiply result
    """
    A = sc.textFile(file_A).map(lambda line: np.array([float(x) for x in line.split(",")])).cache()
    v = sc.textFile(file_v).map(lambda line: np.array([float(x) for x in line.split(",")])).cache()
    A = A.map(lambda x: (x[0], ((x[1+i], i) for i in range(len(x[1:])))))
    A_j = A.flatMap(add_j)
    v = v.flatMap(add_v)
    A_join = A_j.join(v).map(lambda x: (x[1][0][0], x[1][0][1]*x[1][1]))
    multiply = A_join.reduceByKey(lambda a, b: a + b).map(lambda x: x[1]).collect()
    return multiply

if __name__ == "__main__":
    sc = pyspark.SparkContext(appName="matrix")
    matrix_multiply(sys.argv[1], sys.argv[2])
