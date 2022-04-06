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


class Node:
    def __init__(self, key):
        self.val = key
        self.children = []

def count_of_nodes(root, queries, s):
    general_q = deque()
    found_q = deque()
    res = []
    for query in queries:
        general_q.append(root)
        counter = 0
        ####################################################
        while general_q:                        #----
            n = len(general_q)                  #   |
            for i in range(n):                  #   |
                node = general_q.popleft()      #----
                letter = s[node.val-1]
                index = node.val
                if query[0] == index and query[1] == letter:
                    general_q = deque()
                    found_q.extend(node.children)
                    counter += 1
                    break
                else:
                    general_q.extend(node.children)
        ####################################################
        while found_q:
            n = len(found_q)
            for i in range(n):
                node = found_q.popleft()
                letter = s[node.val-1]
                if letter == query[1]: counter += 1
                found_q.extend(node.children)
        ####################################################
        res.append(counter)
    print(res)
    return res
                
class TestCountNodes():
    def setUp(self) -> None:
        pass

    def test_visible_nodes_1(self):
        s_1 = "aba"
        root_1 = Node(1) 
        root_1.children.append(Node(2)) 
        root_1.children.append(Node(3)) 
        queries_1 = [(1, 'a')]
        count_of_nodes(root_1,queries_1,s_1)

    def test_visible_nodes_2(self):
        s_2 = "abaacab"
        root_2 = Node(1)
        root_2.children.append(Node(2))
        root_2.children.append(Node(3))
        root_2.children.append(Node(7))
        root_2.children[0].children.append(Node(4))
        root_2.children[0].children.append(Node(5))
        root_2.children[1].children.append(Node(6))
        queries_2 = [[1, 'a'],[2, 'b'],[3, 'a']]
        count_of_nodes(root_2,queries_2,s_2)

if __name__ == '__main__':
    t = TestCountNodes()
    '''
                1(a)
              /   |  \    
             /    |   \    
            /     |    \
        2(b)     3(a)  7(b)
        / \       |
    2(b)  3(a)   7(b)
    output = [4,1,2]
    '''    
    t.test_visible_nodes_2()
    '''
            1(a)
           /    \
        2(b)    3(a)
    output = [2]
    '''
    t.test_visible_nodes_1()