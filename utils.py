import random
from typing import Optional, List, Tuple

from avl_tree import *


def generate_random_tree(count_el: int = 20, min_val: int = 0, max_val: int = 101) -> Tuple[Optional[AVLNode], List[int]]:
    keys = random.sample(range(min_val, max_val), count_el)
    root = None

    for key in keys:
        root = insert(root, key)

    return root, keys


def show_tree_info(root: Optional[AVLNode], values: List[int]) -> None:
    print("AVL-Tree:")
    print(root)
    print()

    print(f"Generated values: {values}")
    print(f"Sorted value: {sorted(values)}")