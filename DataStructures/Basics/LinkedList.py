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
        # point next/-> to the data
        new_node.next = self.head
        #[Sun]->    [Mon]->...
        #[HEAD]->   [Mon]->...
        
        # point the head to the new node
        self.head = new_node
        #[HEAD]->   [Sun]->...

    def at_end(self, new_node):
        # if the sll is empty
        if self.head is None:
            self.head = new_node
            return
        # if the sll is not empty
        # grab a copy of only data
        last = self.head
        #[Sun]->[Mon]->...
        while(last.next):
            last = last.next
        last.next = new_node

    def in_between(self,middle_node,new_node):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        # grab the data from the middle node until the end
        # the original is [Sun] -> [Mon] -> [Tue] -> [Wed] -> [Thu] -> null
        # the middle_node is [Tue]
        # the data is [Wed] -> [Thu] -> null
        new_node.next = middle_node.next
        # [NewDay] -> [Wed] -> [Thu] -> null

        # the middle node point to the new node
        middle_node.next = new_node
        # ... [Tue] -> [NewDay] -> ...
        # [Sun] -> [Mon] -> [Tue] -> [NewDay] -> [Wed] -> [Thu] -> null

    def remove_node(self, key_to_remove):
        only_data = self.head

        #the key is at the beginning
        if (only_data.data == key_to_remove):
            self.head = only_data.next
            return
        
        #iterate over the sll
        while (only_data is not None):
            if only_data.data == key_to_remove:
                break
            left_side = only_data
            only_data = only_data.next

        # reach the end and not find the key
        if (only_data == None):
            return

        # left_side is [Tue]
        # only_data is [NewDay]
        left_side.next = only_data.next
        # ... [Tue] -> [Wed] -> ...

class build:
    
    def elements(days):
        nodes = []
        for day in days:
            nodes.append(node(day))
        return nodes

    def way1(nodes):
        sll = single_linked_list()

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

    def way2(nodes):
        sll = single_linked_list()

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

    def way3(nodes):
        sll = single_linked_list()

        for ix,node in enumerate(nodes[:-1]):
            node.next = nodes[ix+1]
        
        sll.head = nodes[0]
        
        return sll

if __name__ == '__main__':
    days = ["Mon","Tue","Wed"]

    nodes = build.elements(days)
    sll = build.way1(nodes)
    print('way1')
    sll.show()

    nodes = build.elements(days)
    sll = build.way2(nodes)
    print('way2')
    sll.show()

    nodes = build.elements(days)
    sll = build.way3(nodes)
    print('way3')
    sll.show()

    nn = node("Sun")
    print('at_beginning')
    sll.at_beginning(nn)
    sll.show()

    nn = node("Thu")
    print('at_end')
    sll.at_end(nn)
    sll.show()

    nn = node("NewDay")
    print('in_between')
    # ...[Tue]->...
    sll.in_between(sll.head.next.next,nn)
    sll.show()
    
    sll.remove_node("NewDay")
    sll.show()