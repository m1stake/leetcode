from TreeNodeUtil import TreeNode, make_tree_node


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        return self.tree_height(root)[1]

    def tree_height(self, tree):

        if tree is None:
            return 0, True

        left_height, left_balanced = self.tree_height(tree.left)
        right_height, right_balanced = self.tree_height(tree.right)

        if not (left_balanced and right_balanced):
            return -1, False
        elif abs(left_height - right_height) > 1:
            return -1, False
        else:
            return max(left_height, right_height) + 1, True


print(
    Solution().isBalanced(make_tree_node((3, 9, (20, 15, 7)))),
    Solution().isBalanced(make_tree_node((1, (2, (3, 4, 4), 3), 2)))
)
