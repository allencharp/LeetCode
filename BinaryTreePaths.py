# Total Accepted: 99604
# Total Submissions: 272201
# Difficulty: Easy
# Contributor: LeetCode
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root.left is None and root.right is None:
            return str(root.val)
        elif root.left:
            return str(root.val) + "->" + self.binaryTreePaths(root.left)
        elif root.right:
            return str(root.val) + "->" + self.binaryTreePaths(root.right)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
five = TreeNode(5)
two = TreeNode(2)
three = TreeNode(3)
one = TreeNode(1)
one.right = two
one.left = three
two.right = five

s = Solution()
print(s.binaryTreePaths(one))
