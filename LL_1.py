class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


    # Return middle node. In case of even number of nodes, return higher index node
    def find_middle_node(self):
        middle_node = self.head
        check_node = self.head

        while True:
            if check_node is None or check_node.next is None:
                return middle_node

            check_node = check_node.next.next
            middle_node = middle_node.next


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )

