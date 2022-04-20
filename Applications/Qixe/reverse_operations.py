class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

# General linked list reversal function
def reverseLL(head):
    prev = None
    node = head
    # node.data % 2 == 0 still EVEN
    while node and node.data % 2 == 0:
        temp = node.next
        node.next = prev
        prev = node
        node = temp

    if not node:
        # if the while loop invariant broke due node being None
        nextPart = None
    else:
        # if the while loop invariant broke due node data being odd
        nextPart = node

    return (prev, nextPart)

def reverse(head):
    # Write your code here
    node = head
    prev = dummy = Node("dummy")
    dummy.next = head
    ans = []
    while node:
        # ODD
        if node.data % 2:
            # node data value is odd
            prev = node
            node = node.next
        # EVEN
        else:
            # reverse linked list and 
            # get newHead for the reversed list + node 
            # for the start of next part
            newHead, nextPart = reverseLL(node)
            prev.next = newHead
            node.next = nextPart
            node = node.next
        
    return dummy.next

def createLinkedList(arr):
  head = None
  tempHead = head
  for v in arr:
    if head == None:
      head = Node(v)
      tempHead = head
    else:
      head.next = Node(v)
      head = head.next
  return tempHead

if __name__ == '__main__':
    R = []
    R.append(createLinkedList([1, 2, 8, 9, 12, 16]))
    R.append(createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12]))
    for r in R:
        print(r,reverse(r))
        

    