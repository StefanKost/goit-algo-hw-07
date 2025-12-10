from typing import Optional

from avl_tree import *
from utils import generate_random_tree, show_tree_info


def get_max_node(node: Optional[AVLNode]) -> Optional[AVLNode]:
    if node is None:
        return None

    current = node
    while current.right is not None:
        current = current.right
    return current


if __name__ == "__main__":
    root, keys = generate_random_tree()
    show_tree_info(root, keys)

    max_node = get_max_node(root)
    if max_node:
        print(f"Max value in tree: {max_node.key}")
    else:
        print("Tree is empty")
