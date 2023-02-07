from typing import List, Any


class TreeNode:
    def __init__(self, val: Any, children: List = []) -> None:
        self.val = val
        self.children = children
