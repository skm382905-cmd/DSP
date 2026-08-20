class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node


    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        print("Deleted:", temp.data)


    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


dll = DoublyLinkedList()

dll.insert_begin(10)
dll.insert_begin(20)
dll.insert_begin(30)

dll.display()

dll.delete_begin()

dll.display()
