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
	
	def cacheDecorator(function):
		
		def wrapper(self, *args, **kwargs):
			nums = args[0]
			if len(nums) in self.cacheDict:
				return self.cacheDict[len(nums)]
			else:
				v = function(self, nums)
				self.cacheDict[len(nums)] = v
				return v
		
		return wrapper
	
	@cacheDecorator
	def rob(self, nums):
		if(len(nums) == 0):
			return 0
		elif(len(nums) == 1):
			return nums[0]
		elif(len(nums) == 2):
			return max(nums[0],nums[1])
		else:
			return max(self.rob(nums[:len(nums)-1]), self.rob(nums[:len(nums)-2])+nums[len(nums)-1])
			

s = Solution()
print s.rob([1,2,4,8,1,1,9])