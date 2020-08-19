

class TreeNode:

    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


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

