from TreeNodeUtil import TreeNode, make_tree_node


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:

        left_ = self.left_first(root)
        print(left_)
        right_ = self.right_first(root)
        print(right_)

        return self.left_first(root) == self.right_first(root)

    def left_first(self, node):

        if node is not None:
            if node.left is not None or node.right is not None:
                return node.val, self.left_first(node.left), self.left_first(node.right)
            else:
                return node.val

    def right_first(self, node):
        if node is not None:
            if node.left is not None or node.right is not None:
                return node.val, self.right_first(node.right), self.right_first(node.left)
            else:
                return node.val


print(
    Solution().isSymmetric(make_tree_node((1, (2, 3, 4), (2, 4, 3)))),
    Solution().isSymmetric(make_tree_node((1, (2, 2, None), (2, 2, None)))),
)