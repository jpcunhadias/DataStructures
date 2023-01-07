from nodes import Node

class BinaryTree:
    """
    A binary tree is a tree data structure in which each node has at most two children, 
    which are referred to as the left child and the right child.
    
    
    """
    
    
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def insert(self, value):
        "Insert a value into the tree."
        
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
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

    def search(self, value):
        "Search for a value in the tree."
        if self.root is None:
            return False
        else:
            return self._search(self.root, value)

    def _search(self, current, value):
        if current is None:
            return False
        elif current.value == value:
            return True
        elif current.value > value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)
        
    def delete(self, value):
        "Delete a value from the tree."
        if self.root is None:
            return
        else:
            self.root = self._delete(self.root, value)
            
    def _delete(self, current, value):
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
        
    
    # def print_tree(self):
    #     "Print the tree."
    #     if self.root is None:
    #         print("Empty tree")
    #     else:
    #         self._print_tree(self.root)
            
    # def _print_tree(self, root):
    #     if root is None:
    #         return

    #     nodes = []
    #     nodes.append(root)

    #     while len(nodes) > 0:
    #         current = nodes.pop(0)
    #         print(current.value)
    #         if current.left is not None:
    #             nodes.append(current.left)
    #         if current.right is not None:
    #             nodes.append(current.right)

    def print_tree(self,node, level=0):
        "Print the tree."
        if node is not None:
            self.print_tree(node.right, level+1)
            print(' ' * 4 * level + '->', node.value)
            self.print_tree(node.left, level+1)