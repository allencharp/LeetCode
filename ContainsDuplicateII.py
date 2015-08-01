#Given an array of integers and an integer k, 
#find out whether there there are two distinct 
#indices i and j in the array such that 
#nums[i] = nums[j] and the difference between i and j is at most k.
class Solution:
	# @param {integer[]} nums
	# @param {integer} k
	# @return {boolean}
	def containsNearbyDuplicate(self, nums, k):
		for loc, value in enumerate(nums):
			if(loc is not len(nums)-1):
				isExist = self.containsDuplicateInlenght(value, nums[loc+1:], min(k, len(nums[loc+1:])))
				if(isExist):
					return True
		return False
			
			
	def containsDuplicateInlenght(self,value, num, len):
		
		isExist = False;
		for i in range(len):
			if num[i] == value:
				isExist = True
				break
		return isExist
	
s = Solution()

print s.containsNearbyDuplicate([1,2,3,4,5,1], 4)
