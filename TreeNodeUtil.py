

class TreeNode:

    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return str(left_first_tree_travel(self))


def make_tree_node(tree_desc):
    """
    :param tree_desc like (1, None, (2, 3, None))
    """

    if tree_desc is not None:

        if type(tree_desc) is tuple:
            node_val, left, right = tree_desc

            return TreeNode(node_val, make_tree_node(left), make_tree_node(right))
        else:
            node_val = tree_desc
            return TreeNode(node_val)
    else:
        return None


def left_first_tree_travel(self, node):

    if node is not None:
        if node.left is not None or node.right is not None:
            return node.val, self.left_first(node.left), self.left_first(node.right)
        else:
            return node.val


def right_first_travel(self, node):
    if node is not None:
        if node.left is not None or node.right is not None:
            return node.val, self.right_first(node.right), self.right_first(node.left)
        else:
            return node.val

