import numpy as np


class Tree(object):

   def __init__(self, root = None):
       """
       :param root: tree root
       """
       self.root = root

   def add(self, val):
       """
       :param val: value you need to add to the tree node
       :return: new node children
       """
       if(self.root == None):
           self.root = Node(val)
       else:
           self._add(val, self.root)

   def _add(self, val, node):
       """
       Add node to the tree
       :param val: value you need to add to the tree node
       :param node: node in the tree
       :return: new node children
       """
       if(val < node.value):
           if(node.left != None):
               self._add(val, node.left)
           else:
               node.left = Node(val)
       else:
           if(node.right != None):
               self._add(val, node.right)
           else:
               node.right = Node(val)

   def height(self, node):
       """
       Compute the height of a tree.
       :param node: tree node
       :return: tree height
       """
       if (node == None):
           return 0;
       else:
           return max(self.height(node.left), self.height(node.right)) + 1

   def print_tree(self, root):
        """
        Print Tree with required structure.
        :param root: Tree root
        :return: a binary tree
        """

        def print_output(node, row, left, right):
            if not node:
                return
            center = (left + right) // 2

            self.output[row][center] = str(node.value)
            print_output(node.left, row + 1, left, center - 1)
            print_output(node.right, row + 1, center + 1, right)

        height = self.height(self.root)
        width = 2 ** height -1
        self.output = [['|'] * width for i in range(height)]
        print_output(node = root, row = 0, left = 0, right = width - 1)
        print(np.asarray(self.output))
        return self.output



class Node(object):

   def __init__(self, value):
       self.value = value
       self.left = None
       self.right = None
       self.output = None


if __name__ == '__main__':
    tree = Tree()
    num_nodes = np.random.randint(0, 10, size=4)
    for i in num_nodes:
        tree.add(i)
    result = tree.print_tree(tree.root)




