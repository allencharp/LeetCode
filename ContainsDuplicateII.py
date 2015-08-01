#Given an array of integers and an integer k, 
#find out whether there there are two distinct 
#indices i and j in the array such that 
#nums[i] = nums[j] and the difference between i and j is at most k.
class Solution:
	def __init__(self):
		self.dict = {} # Data Structure :: value : [loc1, loc2, ...]
	
	# @param {integer[]} nums
	# @param {integer} k
	# @return {boolean}
	def containsNearbyDuplicate(self, nums, k):
		for loc, value in enumerate(nums):
			if self.dict.has_key(value):
				self.dict[value].append(loc)
			else:
				self.dict[value] = [loc]
		
		for key,value in self.dict.iteritems():
			if(len(value) <= 1):
				continue
			for loc in range(len(value)):
				if loc - 1 >= 0:
					if (value[loc] - value[loc-1] <= k):
						return True
		return False		
	
s = Solution()

print s.containsNearbyDuplicate([1,2,3,4,5,1], 4)
