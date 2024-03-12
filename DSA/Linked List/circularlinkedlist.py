class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node


    def getlength(self):
        count = 0
        if self.head is None:
            return count
        else:
            ptr = self.head
            while ptr:
                count += 1
                ptr = ptr.next
                if ptr == self.head:
                    print(f"Length of list: {count}")
                    break

    # Function for deleting a node.
    def delete_data(self, data_to_delete):
        if self.head is None:
            return
        
        if self.head.data == data_to_delete:
            self.head = self.head.next
            self.tail.next = self.head
            return
        
        ptr = self.head
        ptr2 = self.head.next
        while ptr.next:
            if ptr2.data == data_to_delete:
                ptr.next = ptr2.next
                break
            ptr2 = ptr2.next
            ptr = ptr.next

    def print_cll(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            ptr = self.head
            while ptr:
                print(f"-> {ptr.data} -> ", end="")
                ptr = ptr.next
                if ptr == self.head:
                    print("HEAD NODE ->")
                    break



if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.add_node(10)
    cll.add_node(11)
    cll.add_node(12)
    cll.add_node(13)
    cll.print_cll()
    cll.delete_data(12)
    cll.print_cll()
    # cll.getlength()