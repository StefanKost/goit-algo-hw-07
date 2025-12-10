from typing import Optional

from avl_tree import *
from utils import generate_random_tree, show_tree_info


def get_min_node(node: Optional[AVLNode]) -> Optional[AVLNode]:
    if node is None:
        return None

    current = node
    while current.left is not None:
        current = current.left
    return current


if __name__ == "__main__":
    root, keys = generate_random_tree()
    show_tree_info(root, keys)

    min_node = get_min_node(root)
    if min_node:
        print(f"Min value in tree: {min_node.key}")
    else:
        print("Tree is empty")
