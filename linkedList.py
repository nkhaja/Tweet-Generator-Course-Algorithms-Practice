#Singly Linked List

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n


    #To test implementation
    def __str__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self):
        self.head = None

    # could alternatively use the set_next method for non base case
    def add(self, data):
        node = Node(data, next=None)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node


    def remove(self, n):
        #Base cases
        if head == None:
            return
        if head.next == None:
            return
        #larger than 1
        if self.head.data == n.data:
            newHead = head.next
            self.head.next = None #Do I need to remove the pointer?
            self.head = newHead

    def size(self):
        current = self.head
        size = 0
        while current:
            size = size + 1
            current = self.head.next
        # could alternatively include size as part of the object

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

def main():
    someList = LinkedList()
    someList.add(1)
    someList.add(2)
    someList.add(3)
    someList.add(20)
    print(someList.find(2))
    print(someList.search(30))
    print(somelist.search(2))



main()
