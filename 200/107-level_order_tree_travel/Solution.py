from TreeNodeUtil import TreeNode, make_tree_node
from typing import List


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        r = []

        self.levelOrderBottom0(root, 0, r)

        r.reverse()

        return r

    def levelOrderBottom0(self, node: TreeNode, level, r):

        if len(r) > level:
            r[level].append(node.val)
        else:
            r.append([node.val])

        if node.left is not None:
            self.levelOrderBottom0(node.left, level + 1, r)

        if node.right is not None:
            self.levelOrderBottom0(node.right, level + 1, r)


print(
    Solution().levelOrderBottom(make_tree_node((3, 9, (20, 15, 7))))
)
