
# Python3 program to print corner
# node at each level of binary tree
from collections import deque
 
# A binary tree node has key, pointer to left
# child and a pointer to right child
class Node:
    def __init__(self, key):
         
        self.key = key
        self.left = None
        self.right = None
 
# Function to print corner node at each level
def printCorner(root: Node):
 
    # If the root is null then simply return
    if root == None:
        return
 
    # Do level order traversal
    # using a single queue
    q = deque()
    q.append(root)
 
    while q:
 
        # n denotes the size of the current
        # level in the queue
        n = len(q)
        for i in range(n):
            temp = q[0]
            q.popleft()
 
            # If it is leftmost corner value or
            # rightmost corner value then print it
            if i == 0 or i == n - 1:
                print(temp.key, end = " ")
 
            # push the left and right children
            # of the temp node
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
 
# Driver Code
if __name__ == "__main__":
     
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
     
    printCorner(root)
 
# This code is contributed by sanjeev2552