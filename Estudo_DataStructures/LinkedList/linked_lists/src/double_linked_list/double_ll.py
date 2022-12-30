from nodes import Node

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """Function to append new node to the end of the list

        Parameters
        ----------
        value : any
            value to be added to the end of the list
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        """Function to prepend new node to the beginning of the list

        Parameters
        ----------
        value : any
            value to be added to the beginning of the list
        """
        
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def insert(self, index, value):
        """Function to insert new node at a specific index of the list

        Parameters
        ----------
        index : int
            index where the new node should be inserted
        value : any
            value to be added to the index of the list
        """
        if index == 0:
            self.prepend(value)
        elif index >= self.size():
            self.append(value)
        else:
            new_node = Node(value)
            current_index = 0
            current_node = self.head
            while current_index < index:
                current_node = current_node.next
                current_index += 1
            new_node.next = current_node.next
            current_node.next = new_node

    def remove(self, node):
        """Function to remove node from the list

        Parameters
        ----------
        node : Node
            node to be deleted from the list
        """
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
            node.next.prev = None
        elif node == self.tail:
            self.tail = node.prev
            node.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            
    def size(self):
        """Function to get the size of the list"""
        
        size = 0
        current_node = self.head
        while current_node is not None:
            size += 1
            current_node = current_node.next
        return size

    def reverse(self):
        """Function to reverse the list"""

        current_node = self.head
        while current_node is not None:
            current_node.prev, current_node.next = current_node.next, current_node.prev
            current_node = current_node.prev
        self.head, self.tail = self.tail, self.head

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=' ')
            current_node = current_node.next
        print('------------------')
        
    def to_list(self):
        """Function to convert the list to a list"""
        result = []
        current_node = self.head
        while current_node is not None:
            result.append(current_node.value)
            current_node = current_node.next
        return result        

