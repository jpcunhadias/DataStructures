from Estudo_DataStructures.trees.nodes import Node
from typing import Union


class BinaryTree:
    """
    A binary tree is a tree data structure in which each node has at most two children, 
    which are referred to as the left child and the right child.
    
    The greater children are on the right and the lesser children are on the left of the parent node.
    
    """

    def __init__(self, root_value: int = None):
        self.root = Node(root_value) if root_value is not None else None

    def insert(self, value: int) -> None:
        """
        The insert function takes a value and inserts it into the tree.
        It does this by calling _insert, which is a recursive function that
        traverses the tree until it finds an empty node to insert the value.

        :param self: Refer to the object itself
        :param value:int: Store the value of the node that is being inserted into the tree
        :return: Nothing
        :doc-author: Trelent
        """

        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current: Node, value: int) -> None:
        if current.value > value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        elif current.value < value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)
        else:
            # value is already in the tree
            pass

    def search(self, value: int) -> Union[bool, Node]:
        """
        The search function takes a value and searches the tree for that value.
        If it finds the value, it returns True. If not, it returns False.

        :param self: Access the class attributes'
        :param value:int: Store the value of the node that is being searched for
        :return: The node that contains the value we are searching for
        :doc-author: Trelent
        """

        if self.root is None:
            return False
        else:
            return self._search(self.root, value)

    def _search(self, current: Node, value: int) -> Union[bool, Node]:
        if current is None:
            return False
        elif current.value == value:
            return True
        elif current.value > value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)

    def find_smallest(self, root: Node) -> Union[None, Node]:
        """
        The find_smallest function finds the smallest value in the tree.
        It does this by calling _find_smallest, which is a recursive function that
        traverses the tree until it finds the smallest value.

        :param self: Access the attributes and methods of the class
        :param root: Traverse the tree
        :return: The smallest value in the tree
        :doc-author: Trelent
        """

        if self.root is None:
            return None
        else:
            return self._find_smallest(root)

    def _find_smallest(self, node: Node) -> Node:
        """
        The _find_smallest function finds the smallest value in a given tree.
        It does this by recursively traversing through the left side of each node until it reaches
        the end, at which point it returns that node's value. It is called from within the find_smallest function.

        :param self: Access the class attributes
        :param node:Node: Traverse the tree
        :return: The smallest value in the tree
        :doc-author: Trelent
        """

        if node.left:
            return self._find_smallest(node.left)
        return node

    def delete(self, value: int) -> None:
        """
        The delete function takes a value as input and searches the tree for that value. If it finds the value,
        it deletes that node from the tree. If not, then we return None.

        :param self: Access the attributes and methods of the class
        :param value:int: Tell the function what value to delete
        :return: None
        :doc-author: Trelent
        """

        if self.root is None:
            return
        else:
            self.root = self._delete(self.root, value)

    def _delete(self, current: Node, value: int) -> Union[None, Node]:
        """
        The _delete function takes a node and a value as arguments.
        If the node is None, it returns None.
        Otherwise, if the current node's value is greater than the given value,
        it recursively calls _delete on its left child with the same arguments.
        If that call returns something other than None, it sets that return to be
        the current node's new left child (because we're deleting from its right subtree).
        Otherwise, (if _delete returned None), then we know that either:

        1) there was no left child;
        or
        2) all of our left subtree was deleted and

        :param self: Reference the object itself
        :param current:Node: Keep track of the current node
        :param value:int: Store the value of the node that is to be deleted
        :return: The node that was deleted
        :doc-author: Trelent
        """
        """"""

        if current is None:
            return None
        elif current.value > value:
            current.left = self._delete(current.left, value)
        elif current.value < value:
            current.right = self._delete(current.right, value)
        else:
            # current.value == value
            if current.left is None and current.right is None:
                # current is a leaf
                current = None
            elif current.left is None:
                # current has no left child
                current = current.right
            elif current.right is None:
                # current has no right child
                current = current.left
            else:
                # current has two children
                # find the smallest value in the right subtree
                smallest = self._find_smallest(current.right)
                current.value = smallest.value
                current.right = self._delete(current.right, smallest.value)
        return current

    def print_tree(self, node: Node, level: int = 0):
        """
        The print_tree function prints out the values of tree nodes in a hierarchical order.
        For example, the following code:
            print_tree(my_tree)
        will produce this output:

        :param self: Reference the class itself
        :param node: Keep track of the current node
        :param level: Keep track of the level in the tree
        :return: The binary tree in a hierarchical structure
        :doc-author: Trelent
        """

        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.print_tree(node.left, level + 1)
