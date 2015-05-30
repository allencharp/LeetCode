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
		if(len(nums) == 0):
			return 0
		elif(len(nums) == 1):
			return nums[0]
		elif(len(nums) == 2):
			return max(nums[0],nums[1])
		elif(len(nums) == 3):
			return max(nums[1], nums[0]+nums[2])
		
		maxLoc, maxValue = self.getMaxAndLoc(nums)
		if(maxLoc == 0):
			next_nums = nums[maxLoc + 2:]
			_,nextMax = self.getMaxAndLoc(next_nums)
			return maxValue + nextMax
		elif(maxLoc == len(nums)-1):
			next_nums = nums[:len(nums) - 2:]
			_,nextMax = self.getMaxAndLoc(next_nums)
			return maxValue + nextMax
		else:
			next_nums = nums[0:maxLoc-1] + nums[maxLoc+2: len(nums)]
			_,nextMax = self.getMaxAndLoc(next_nums)
			return max(maxValue + nextMax, nums[maxLoc-1]+nums[maxLoc+1])
		
	def getMaxAndLoc(self, num):
		maxValue = 0
		maxLoc = 0
		for i, val in enumerate(num):
			if(val > maxValue):
				maxValue = val
				maxLoc = i
		return (maxLoc, maxValue)

s = Solution()
print s.rob([2,7,9,3,1])