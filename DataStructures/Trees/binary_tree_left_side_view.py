"""
There is a binary tree with N nodes. You are viewing the tree from its left side and can see only the leftmost nodes
at each level. Return the number of visible nodes.
Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. The leftmost node at a
level could be a right node.
Signature
int visibleNodes(Node root) {
Input
The root node of a tree, where the number of nodes is between 1 and 1000, and the value of each node is between
0 and 1,000,000,000
Output
An int representing the number of visible nodes.
Example
            8  <------ root
           / \
         3    10
        / \     \
       1   6     14
          / \    /
         4   7  13
output = 4
leftmost nodes = 8,3,1,4
"""
from collections import deque
from unittest import TestCase


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Add any helper functions you may need here


def visible_nodes(root):
    if not root:
        return 0
    q = deque()
    q.append(root)
    res = []
    while q:                        #----
        n = len(q)                  #   |
        for i in range(n):          #   |
            node = q.popleft()      #----
            if i == 0:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return len(res)


class TestVisibleNodes():
    def setUp(self) -> None:
        pass

    def test_visible_nodes_1(self):
        root_1 = TreeNode(8)
        root_1.left = TreeNode(3)
        root_1.right = TreeNode(10)
        root_1.left.left = TreeNode(1)
        root_1.left.right = TreeNode(6)
        root_1.left.right.left = TreeNode(4)
        root_1.left.right.right = TreeNode(7)
        root_1.right.right = TreeNode(14)
        root_1.right.right.left = TreeNode(13)
        visible_nodes(root_1)

    def test_visible_nodes_2(self):
        root_2 = TreeNode(10)
        root_2.left = TreeNode(8)
        root_2.right = TreeNode(15)
        root_2.left.left = TreeNode(4)
        root_2.left.right = TreeNode(6)
        root_2.left.left.right = TreeNode(5)
        root_2.left.left.right.right = TreeNode(6)
        root_2.right.left = TreeNode(14)
        root_2.right.right = TreeNode(16)
        visible_nodes(root_2)

if __name__ == '__main__':
    t = TestVisibleNodes()
    '''
            8
           / \
         3    10
        / \     \
       1   6     14
          / \    /
         4   7  13
    output = 4
    leftmost nodes = 8,3,1,4
    '''
    t.test_visible_nodes_1()
    '''
             10
           /   \
          8     15
        /  \   /  \
       4    6 14   16
        \   
         5  
          \ 
           6
    output = 5
    leftmost nodes = 10,8,4,5,6
    '''    
    t.test_visible_nodes_2()