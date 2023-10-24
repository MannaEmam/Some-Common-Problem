# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def morris_traversal(root):
#     current = root
#
#     while current:
#         if current.left is None:
#             print(current.data, end=" ")
#             current = current.right
#         else:
#             # Find the inorder predecessor of current
#             pre = current.left
#             while pre.right and pre.right != current:
#                 pre = pre.right
#
#             # Make current as the right child of its inorder predecessor
#             if pre.right is None:
#                 pre.right = current
#                 current = current.left
#             # Revert the changes made to restore the original tree and print current node
#             else:
#                 pre.right = None
#                 print(current.data, end=" ")
#                 current = current.right

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def morris_inorder_traversal(root):
    curr = root
    while curr:
        if not curr.left:
            print(curr.data, end=" ")
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right is not curr:
                pre = pre.right
            if not pre.right:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                print(curr.data, end=" ")
                curr = curr.right


def morris_preorder_traversal(root):
    curr = root
    while curr:
        if not curr.left:
            print(curr.data, end=" ")
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right is not curr:
                pre = pre.right
            if pre.right is curr:
                pre.right = None
                curr = curr.right
            else:
                print(curr.data, end=" ")
                pre.right = curr
                curr = curr.left


# Driver program to test above functions
if __name__ == '__main__':
    """
	Constructed binary tree is
		    1
		/ \
		2	 3
	/ \
	4	 5
	"""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    morris_inorder_traversal(root)
    print()
    morris_preorder_traversal(root)
