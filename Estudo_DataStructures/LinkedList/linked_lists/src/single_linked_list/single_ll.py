from nodes import Node

class SingleLinkedList:
    
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
        new_node.next = self.head
        self.head = new_node
    
    def length(self):
        """Function to get the length of the list

        Returns
        ----------
        length : int
            length of the list"""
            
        if self.head is None:
            return 0
        
        current_node = self.head
        total_length = 0
        
        while current_node is not None:
            total_length += 1
            current_node = current_node.next
        return total_length
    
    def to_list(self):
        """Function to convert the list to a list of values

        Returns
        ----------
        list_of_values : list
            list of values"""
        
        node_data = []
        current_node = self.head
        
        while current_node is not None:
            node_data.append(current_node.value)
            current_node = current_node.next
            
        return node_data
    
    def print_list(self):
        """Function to print the list"""
        
        current_node = self.head
        
        if current_node is None:
            message = "List is empty"
            print(message)
            return
            
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
        print('-----------------------')
        
    def reverse_list(self):
        """Function to reverse the list"""
        
        previous_node = None
        current_node = self.head
        
        if current_node is None:
            message = "List is empty"
            print(message)
            return
        
        while current_node is not None:
            """Reversing the list"""
            
            next = current_node.next 
            current_node.next = previous_node
            previous_node = current_node
            current_node = next
            
        self.head = previous_node
        
