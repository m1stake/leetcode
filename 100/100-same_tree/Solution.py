from TreeNodeUtil import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if p is not None and q is not None:
            return self.isSameTree(p.left, q.left) \
                and p.val == q.val \
                and self.isSameTree(p.right, q.right)
        elif p is not None and q is None:
            return False
        elif p is None and q is not None:
            return False
        else:
            return True

