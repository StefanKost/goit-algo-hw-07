from typing import Optional

from avl_tree import *
from utils import generate_random_tree, show_tree_info


def get_sum_of_nodes(node: Optional[AVLNode]) -> int:
    if node is None:
        return 0
    return node.key + get_sum_of_nodes(node.left) + get_sum_of_nodes(node.right)


if __name__ == "__main__":
    root, keys = generate_random_tree()
    show_tree_info(root, keys)

    total = get_sum_of_nodes(root)
    if total:
        print(f"Total sum of values: {total}")
    else:
        print("Tree is empty")
