# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and 
# it will automatically contact the police if two adjacent houses were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of 
# money you can rob tonight without alerting the police.
# 
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.

class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def rob(self, nums):
		nums_1 = [v for i,v in enumerate(nums) if i%2 == 1]
		nums_2 = [v for i,v in enumerate(nums) if i%2 == 0]
		
		return max(sum(nums_1), sum(nums_2))
		

s = Solution()
print s.rob([2,7,9,3,1])