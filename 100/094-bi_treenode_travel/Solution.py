from typing import List
from TreeNodeUtil import TreeNode


class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:

        r = []

        if root is not None:
            r += self.inorderTraversal(root.left)
            r.append(root.val)
            r += self.inorderTraversal(root.right)

        return r


tree = TreeNode(1)
right = TreeNode(2)
right_left = TreeNode(3)
right.left = right_left
tree.right = right

print(
    Solution().inorderTraversal(tree),
)
