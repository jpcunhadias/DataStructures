from typing import List, Any


class TreeNode:
    def __init__(self, val: Any, children=None) -> None:
        if children is None:
            children = []
        self.val = val
        self.children = children
