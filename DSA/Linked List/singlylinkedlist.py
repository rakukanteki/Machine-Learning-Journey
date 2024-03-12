# Creating a Node.
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


# Creating a Singly Linked List Class.
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    # Function for inserting at begining.
    def InsertAtBegin(self, data):
        new_node = Node(data)
        # Base Case
        if self.head is None:  # There is no node.
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    # Function for inserting at ending.
    def InsertAtEnd(self, data):
        new_node = Node(data)
        ptr = self.head
        if self.head is None:
            self.head = new_node
            return
        else:
            while ptr.next:
                ptr = ptr.next
            temp = ptr.next
            ptr.next = new_node
            new_node.next = temp
    
    # Function for determining the length of the linked list.
    def getlength(self):
        count = 0
        ptr = self.head
        while ptr:
            count += 1
            ptr = ptr.next
        return count

    # Function for inserting at an index.
    def InserAtAnIndex(self, data, index):
        new_node = Node(data)
        ptr = self.head
        if index<0 or index>self.getlength():
            raise Exception("Invalid index input.")
        
        if index==0:
            self.InsertAtBegin(data)
        
        count = 0
        while ptr:
            if count == index - 1:
                temp = ptr.next
                ptr.next = new_node
                new_node.next = temp
                break
            ptr = ptr.next
            count += 1

    # Function for inserting a list of datas.
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


    # Function for inserting after values.
    def insert_after_values(self, data_after, data_to_insert):
        new_node = Node(data_to_insert)
        if self.head is None:
            return
        if self.head.data == data_after:
            temp = self.head.next
            self.head.next = new_node
            new_node.next = temp
        else:
            ptr = self.head
            while ptr:
                if ptr.data == data_after:
                    temp = ptr.next
                    ptr.next = new_node
                    new_node.next = temp
                    break
                ptr = ptr.next
    

    # Function for deleting a node.
    def delete_at(self, index):
        if index<0 or index>self.getlength():
            raise Exception("Invalid Index input.")
        if self.head is None:
            print("Linked list is already empty.")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        ptr = self.head
        while ptr.next:
            if count == index - 1:
                ptr.next = ptr.next.next
                break

            ptr = ptr.next
            count += 1
    

    # Function for deleting a node by value.
    def delete_by_value(self, data_to_delete):
        if self.head is None:
            return
        if self.head.data == data_to_delete:
            self.head = self.head.next
            return
        ptr = self.head
        while ptr.next:
            if ptr.next.data == data_to_delete:
                ptr.next = ptr.next.next
                break
            ptr = ptr.next


    # Function for printing.
    def print_sll(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            ptr = self.head
            while ptr:
                print(f"{ptr.data} -> ", end="")
                ptr = ptr.next


if __name__ == "__main__":
    sll = SinglyLinkedList()
    # sll.InsertAtBegin(30)
    # sll.InsertAtBegin(20)
    sll.InsertAtBegin(10)
    # sll.InsertAtEnd(40)
    # sll.InserAtAnIndex(69, 2)
    sll.insert_values([12, 23 ,21, 32, 22])
    # sll.insert_after_values(21, 69)
    # sll.delete_at(3)
    # sll.delete_by_value(21)
    sll.print_sll()