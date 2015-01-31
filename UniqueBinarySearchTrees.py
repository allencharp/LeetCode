# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
# 
# For example,
# Given n = 3, there are a total of 5 unique BST's.
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# http://en.wikipedia.org/wiki/Catalan_number
# Catalan number

class Solution:
	# @return an integer
	def numTrees(self, n):
		if n == 0:
			return 1
		elif(n == 1 or n == 2):
			return n;
		else:
			rtn = 0
			
			for i in range(n):
				rtn  = rtn + self.numTrees(i)* self.numTrees(n-i-1)
			
			return rtn
		
		
s = Solution()
print s.numTrees(4)