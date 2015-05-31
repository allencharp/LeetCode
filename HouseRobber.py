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
	
	def __init__(self):
		self.cacheDict = {}
	
	# @param {integer[]} nums
	# @return {integer}
	def rob(self, nums):
		if(len(nums) == 0):
			return 0
		elif(len(nums) == 1):
			return nums[0]
		elif(len(nums) == 2):
			if not len(nums) in self.cacheDict:
				self.cacheDict[len(nums)] = max(nums[0],nums[1])
				return max(nums[0],nums[1])
			else:
				return self.cacheDict[len(nums)]
		else:
			if not len(nums) in self.cacheDict:
				self.cacheDict[len(nums)] = max(self.rob(nums[:len(nums)-1]), self.rob(nums[:len(nums)-2])+nums[len(nums)-1])
				return max(self.rob(nums[:len(nums)-1]), self.rob(nums[:len(nums)-2])+nums[len(nums)-1])
			else:
				return self.cacheDict[len(nums)]
		

s = Solution()
print s.rob([1,1])