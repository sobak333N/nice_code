from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    


def generate_tree(tree_array: List[Optional[int]], index: int):
    if index > len(tree_array) or tree_array[index] is None:
        return None
    node = TreeNode(val=tree_array[index])
    node.left = generate_tree(tree_array, 2*index+1)
    node.right = generate_tree(tree_array, 2*index+2)
    return node


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.recoursive_stack = []
        self.recoursive_stack.append(root)
        self.generate_stack(root)

    def generate_stack(self, node: Optional[TreeNode]):
        if not node:
            return
        while node.left:
            self.recoursive_stack.append(node.left)
            node = node.left

    def next(self) -> int:
        node = self.recoursive_stack[-1]
        val = node.val 

        self.recoursive_stack.pop()
        if node.right:
            self.recoursive_stack.append(node.right)
            self.generate_stack(node.right)


        return val

    def hasNext(self) -> bool:
        return True if self.recoursive_stack else False
        ...


def main():
    tree_arr = [7, 3, 15, None, None, 9, 20]
    root = generate_tree(tree_arr, 0)
    
    bsti_iterator = BSTIterator(root)
    for _ in range(100):
        param_1 = bsti_iterator.next()
        print(param_1)

main()