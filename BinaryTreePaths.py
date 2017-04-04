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
    def __init__(self):
        self.rtnList = []
        self.stack = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        temp = root
        while temp:
            self.stack.append(temp)
            if temp.left:
                temp = temp.left
                continue
            elif temp.right:
                temp = temp.right
                continue
            else:
                self.rtnList.append(format_stack_val())
                self.stack.pop()
                temp = self.stack[len(self.stack)-1]

    def format_stack_val(self):
        return "->".join(self.stack)



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
five = TreeNode(5)
two = TreeNode(2)
three = TreeNode(3)
one = TreeNode(1)
one.left = two
one.right = three
two.right = five

s = Solution()
#print(s.binaryTreePaths(one))
a = ["aaa","bbb"]


def format_stack_val(a):
    return "->".join(a)
print(format_stack_val(a))