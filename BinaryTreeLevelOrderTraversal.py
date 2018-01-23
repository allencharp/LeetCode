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
class Solution(object):
    def levelOrder(self, root):

        pos = 0

        level = 0

        rtnList = []

        while root[pos] is not None:
            times = 2**level
            for i in range(times):


        return rtnList
