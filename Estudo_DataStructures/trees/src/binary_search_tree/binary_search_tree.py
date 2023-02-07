from Estudo_DataStructures.trees.nodes import Node


class BinarySearchTree:
    """Binary Search Tree implementation in Python.
    
    a Binary Search Tree is a node-based binary tree data structure which has the following properties:
    
    1. The left subtree of a node contains only nodes with keys lesser than the node's key.
    2. The right subtree of a node contains only nodes with keys greater than the node's key.
    3. The left and right subtree each must also be a binary search tree.
    4. There must be no duplicate nodes.
    5. The tree is empty or the root node is the only node in the tree.
    
    """

    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        """
        The insert function takes a value and inserts it into the tree. If the value is less than the current node, then
        it goes to its left child. Otherwise, it goes to its right child.

        :param self: Reference the object itself
        :param value:int: Specify the value of the node to be inserted
        :return: None
        :doc-author: Trelent
        """

        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                current_node = current_node.right

    def search(self, value: int) -> Node:
        """
        The search function takes in a value and returns the node with that value. If no such node exists,
        it returns None.

        :param self: Reference the object that is being created
        :param value:int: Search for a value in the tree
        :return: The node with the given value
        :doc-author: Trelent
        """

        if self.root is None:
            return None
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def delete(self, value: int) -> None:
        """
        The delete function takes a value as input and searches for the node with that value. If it finds the node,
        it will delete that node from the tree. If there is no such node, then nothing happens.

        :param self: Reference the current instance of the class
        :param value:int: Store the value of the node that is to be deleted
        :return: None
        :doc-author: Trelent
        """

        if self.root is None:
            return
        current_node = self.root
        parent_node = None
        while current_node is not None:
            if value == current_node.value:
                # node to be deleted has been found
                if current_node.left is None and current_node.right is None:
                    # node is a leaf
                    if parent_node is None:
                        self.root = None
                    elif parent_node.left == current_node:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                    return
                elif current_node.left is None or current_node.right is None:
                    # node has one child
                    if current_node.left:
                        child = current_node.left
                    else:
                        child = current_node.right
                    if parent_node is None:
                        self.root = child
                    elif parent_node.left == current_node:
                        parent_node.left = child
                    else:
                        parent_node.right = child
                    return
                else:
                    # node has two children
                    # find the successor (the smallest node in right subtree)
                    successor_node = current_node.right
                    successor_parent_node = current_node
                    while successor_node.left is not None:
                        successor_parent_node = successor_node
                        successor_node = successor_node.left
                    # replace current node with successor
                    current_node.value = successor_node.value
                    # delete the successor
                    if successor_parent_node.left == successor_node:
                        successor_parent_node.left = None
                    else:
                        successor_parent_node.right = None
                    return
            elif value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
