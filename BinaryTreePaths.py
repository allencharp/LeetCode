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

        if root is None:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]


        temp = root

        current_node_from_stack = False

        while temp:
            self.stack.append(temp)
            if temp.left:
                temp = temp.left
                self.stack[len(self.stack)-1].left = None
                current_node_from_stack = False
                continue
            elif temp.right:
                temp = temp.right
                self.stack[len(self.stack) - 1].right = None
                current_node_from_stack = False
                continue
            else:
                if len(self.stack) < 2:
                    break
                if not current_node_from_stack:
                    self.rtnList.append(self.format_stack_val())

                self.stack.pop()

                temp = self.stack.pop()
                current_node_from_stack = True

        return self.rtnList

    def format_stack_val(self):
        return "->".join([str(item.val) for item in self.stack])



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
print(s.binaryTreePaths(five))
#a = ["aaa","bbb"]
