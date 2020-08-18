from TreeNodeUtil import TreeNode


class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        return self.maxDepth0(root, 0)

    def maxDepth0(self, node: TreeNode, depth: int):

        if node is not None:
            depth += 1
            left_depth = self.maxDepth0(node.left, depth)
            right_depth = self.maxDepth0(node.right, depth)
            return max(left_depth, right_depth)
        else:
            return depth
