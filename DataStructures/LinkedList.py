class node:
    
    def __init__(self, data=None):
        # [data] -> next
        self.data = data
        self.next = None

class single_linked_list:
    
    def __init__(self):
        self.head = None

    def show(self):
        current = self.head
        while current is not None:
            print(f'[{current.data}] -> ', end='')
            current = current.next
        print('null')

    def at_beginning(self,new_node):
        new_node.next = self.head
        #[Sun]->[Mon]->[Tue]->[Wed]->
        #[HEAD]->[Mon]->[Tue]->[Wed]->
        self.head = new_node
        #[HEAD]->[Sun]->[Mon]->[Tue]->[Wed]->

class build:
    
    def elements():
        sll = single_linked_list()
        nodes = []
        nodes.append(node("Mon"))
        nodes.append(node("Tue"))
        nodes.append(node("Wed"))
        return sll,nodes

    def way1(sll,nodes):
        #set a node to the head
        sll.head = nodes[0]
        #[HEAD]->[Mon]->

        # Link first Node to second node
        sll.head.next = nodes[1]
        #[HEAD]->[Mon]->[Tue]->
        
        # Link second Node to third node
        nodes[1].next = nodes[2]
        #[HEAD]->[Mon]->[Tue]->[Wed]->
        
        return sll

    def way2(sll,nodes):

        # Link second Node to third node
        nodes[1].next = nodes[2]
        #[Tue]->[Wed]->
        
        # Link first Node to second node
        nodes[0].next = nodes[1]
        #[Mon]->[Tue]->[Wed]->

        #set a node to the head
        sll.head = nodes[0]
        #[HEAD]->[Mon]->[Tue]->[Wed]->

        return sll

if __name__ == '__main__':
    sll,nodes = build.elements()
    sll = build.way1(sll,nodes)
    print('glue1')
    sll.show()

    sll,nodes = build.elements()
    sll = build.way1(sll,nodes)
    print('glue2')
    sll.show()

    nn = node("Sun")
    sll.at_beginning(nn)
    sll.show()
    
