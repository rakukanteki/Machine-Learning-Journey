class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    # Function for inserting at the begining.
    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        
    # Insertion at end.
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_node
            new_node.prev = ptr.next
    
    # Function for determining the length of the linked list.
    def getlength(self):
        count = 0
        ptr = self.head
        while ptr:
            count += 1
            ptr = ptr.next
        return count
    

    # Insertion at an index.
    def insert_at_an_index(self, data, index):
        new_node = Node(data)
        if index<0 or index>self.getlength():
            raise Exception("Invalid index insertion.")
        if index == 0:
            self.head = new_node
        ptr = self.head
        count = 0
        while ptr.next:
            if count == index - 1:
                temp = ptr.next
                ptr.next = new_node
                new_node.prev = ptr
                new_node.next = temp
                break
            ptr = ptr.next
            count += 1


    # Inserting list.
    def insert_values(self, data_list):
        if self.head is None:
            for data in data_list:
                self.InsertAtEnd(data)
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            for data in data_list:
                ptr.next = Node(data)
                ptr = ptr.next
    
    # Function for removing data.
    def remove_at(self, index):
        if index<0 or index>self.getlength():
            raise Exception("Invalid Index input.")
        if index == 0:
            self.head = self.head.next
            return
        
        ptr1 = self.head
        while index != 1:
            ptr1 = ptr1.next
            index -= 1
        ptr2 = ptr1.next
        ptr1.next = ptr2.next
        ptr2.next.prev = ptr1


    # Remove by value.
    def remove_by_value(self, data_to_delete):
        if self.head is None:
            print("Linked List is empty")
        if self.head.data == data_to_delete:
            self.head = self.head.next
            return
        
        ptr1 = self.head
        while ptr1.next:
            if ptr1.next.data == data_to_delete:
                ptr2 = ptr1.next
                ptr1.next = ptr2.next
                ptr2.next.prev = ptr1
                break
            ptr1 = ptr1.next
        

    def print_dll(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            ptr = self.head
            while ptr:
                print(f"{ptr.data} <=> ", end="")
                ptr = ptr.next


if __name__ == "__main__":
    dll = DoublyLinkedList()
    # dll.insert_at_begin(30)
    # dll.insert_at_begin(20)
    dll.insert_at_begin(10)
    # dll.insert_at_end(69)
    # dll.insert_at_an_index(70, 2)
    # dll.insert_at_an_index(71, 4)
    dll.insert_values([25, 27, 20, 13, 1, 56, 57])
    # dll.remove_at(3)
    dll.remove_by_value(20)
    dll.remove_by_value(27)
    dll.remove_by_value(1)
    dll.print_dll()