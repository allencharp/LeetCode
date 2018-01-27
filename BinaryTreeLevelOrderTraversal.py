#
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# maintain two lists:
# one is for the return value
# one is maintain the binary tree level
class Solution(object):
    def levelOrder(self, root):
        rtn, level = [],[root]
        while level:
            rtn.append([node.val for node in level])

            for node in level:
                level.extend([node.left, node.right])

s = Solution()
print(s.levelOrder([3,9,20,"null","null",15,7]))