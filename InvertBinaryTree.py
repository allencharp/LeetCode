# Invert a binary tree.
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
    # def invertTree(self, root):
    #     if root is None or \
    #             (root.left is None and root.right is None):
    #         return root
    #     else:
    #         root.right,root.left = self.invertTree(root.left),self.invertTree(root.right)



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left
root.right = right
left1 = TreeNode(4)
left.left = left1
right1 = TreeNode(5)
left.right = right1

s = Solution()
print(s.invertTree(root))

