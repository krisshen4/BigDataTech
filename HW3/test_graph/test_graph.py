import unittest
from graph import graph


class TestGraph(unittest.TestCase):

    def test_1(self):
        result = graph.find_shortest_path("path1.txt", 2., 3.)
        answer = ([2.0, 5.0, 6.0, 3.0], 5.0)
        assert result == answer

    def test_2(self):
        result = graph.find_shortest_path("path2.txt", 2., 4.)
        answer = ([], inf)
        assert result == answer

    def test_3(self):
        result = graph.find_negative_cicles("path3.txt")
        answer = [[1., 2., 3., 4., 1.], [2., 3., 4., 1., 2.],
                   [3., 4., 1., 2., 3.], [4., 1., 2., 3., 4.]]
        assert result in answer
