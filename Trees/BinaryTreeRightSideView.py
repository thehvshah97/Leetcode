from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeRightSideView:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([(root, 0)])
        answer = []
        while queue:
            node, index = queue.popleft()
            if node:
                if len(answer) <= index:
                    answer.append(node.val)
                else:
                    answer[index] = node.val
                queue.append([node.left, index + 1])
                queue.append([node.right, index + 1])
        return answer

if __name__ == "__main__":
    treeNode = TreeNode(1)
    treeNode.left = TreeNode(2)
    treeNode.right = TreeNode(3)
    treeNode.left.left = TreeNode(4)
    treeNode.left.right = TreeNode(5)
    print(BinaryTreeRightSideView().rightSideView(treeNode))