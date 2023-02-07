from tree_nodes import TreeNode

class Tree:
    def __init__(self, root_val: int = None) -> None:
        self.root = TreeNode(root_val)

    def add_child(self, val: int) -> None:
        new_node = TreeNode(val)
        self.root.children.append(new_node)
