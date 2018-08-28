import unittest
from HW3.graph import find_shortest_path, find_negative_cycles


class TestGraph(unittest.TestCase):

    def test_1(self):
        result = find_shortest_path("path1.txt", 2., 3.)
        answer = ([2.0, 5.0, 6.0, 3.0], 5.0)
        assert result == answer

    def test_2(self):
        result = find_shortest_path("path2.txt", 2., 4.)
        answer = ([], float("inf"))
        assert result == answer

    def test_3(self):
        result = find_negative_cycles("path3.txt")
        answer = [[1., 2., 3., 4., 1.], [2., 3., 4., 1., 2.],
                   [3., 4., 1., 2., 3.], [4., 1., 2., 3., 4.]]
        assert result in answer

    def test_4(self):
        result = find_negative_cycles("path4.txt")
        answer = []
        assert result == answer
