import unittest

import numpy as np
import numpy.testing as npt

from tree import Tree, Node


class TestTree(unittest.TestCase):

    def test_root_none(self):
        """
        Test when the root is none.
        :return:
        """
        tree = Tree()
        result = tree.print_tree(tree.root)
        assert result == []

    def test_balanced(self):
        """
        Test a balanced tree.
        :return:
        """
        tree = Tree()
        tree.add(10)
        tree.add(11)
        tree.add(12)
        result = tree.print_tree(tree.root)
        assert result == [['|' ,'|' ,'|' ,'10' ,'|' ,'|' ,'|'],
                          ['|' ,'|' ,'|' ,'|' ,'|' ,'11' ,'|'],
                          ['|' ,'|' ,'|', '|' ,'|' ,'|' ,'12']]

    def test_unbalanced(self):
        """
        Test a unbalanced tree.
        :return:
        """
        tree = Tree()
        tree.add(10)
        tree.add(11)
        tree.add(12)
        tree.add(13)
        result = tree.print_tree(tree.root)
        assert result == [['|' ,'|', '|', '|', '|', '|', '|', '10', '|', '|', '|', '|', '|', '|', '|'],
                         ['|' ,'|' ,'|' ,'|' ,'|', '|', '|', '|', '|', '|', '|', '11', '|' ,'|' ,'|'],
                         ['|', '|', '|', '|', '|', '|' ,'|' ,'|', '|', '|', '|', '|', '|', '12' ,'|'],
                         ['|' ,'|', '|' ,'|', '|', '|', '|', '|', '|', '|' ,'|' ,'|' ,'|' ,'|' ,'13']]

