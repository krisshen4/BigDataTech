from pyspark import SparkConf, SparkContext


def matrix_multiply(A, v):
    conf = SparkConf()
    sc = SparkContext(conf=conf)
    A = sc.textFile(A)
    v = sc.textFile(v)
    A = A.map(lambda l: [float(i) for i in l.split(',')])
    A = A.zipWithIndex()
    A = A.map(lambda l: (l[1], [(col, item) for col, item in enumerate(l[0])]))
    A = A.flatMapValues(lambda l: [i for i in l]).map(lambda l: (l[1][0], (l[0], l[1][1])))
    v = v.flatMap(lambda l: [float(i) for i in l.split(',')])
    v = v.zipWithIndex()
    v = v.map(lambda l: (l[1], l[0]))
    Av = A.join(v)
    Av = Av.map(lambda l: (l[1][0][0], l[1][0][1] * l[1][1]))
    Av = Av.reduceByKey(lambda n1, n2: n1 + n2)
    Av = Av.map(lambda l: l[1])
    return Av


if __name__ == '__main__':
    result = matrix_multiply('A.txt', 'v.txt')
    print(result.collect())
