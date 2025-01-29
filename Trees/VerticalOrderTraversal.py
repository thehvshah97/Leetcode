from collections import defaultdict, deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class VerticalOrderTraversal:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        column_table = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, column = queue.popleft()

            if node is not None:
                column_table[column].append(node.val)
                queue.append([node.left, column - 1])
                queue.append([node.right, column + 1])

        return [column_table[x] for x in sorted(column_table.keys())]


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(VerticalOrderTraversal().verticalOrder(root))
