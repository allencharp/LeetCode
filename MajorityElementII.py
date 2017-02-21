# Given an integer array of size n, find all elements that appear
# more than [n/3] times. The algorithm should run in linear time and in O(1) space.

class Solution(object):
	def __init__(self):
		self.store_dict = {}
		
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		nums_len = len(nums)
		return_list = []
		for v in nums:
			if self.store_dict.has_key(v):
				self.store_dict[v] = self.store_dict[v] + 1
			else:
				self.store_dict[v] = 1
				
		
		for key in self.store_dict:
			if self.store_dict[key] > nums_len / 3:
				return_list.append(key)
				
		return return_list
	
s = Solution()
print s.majorityElement([1,1,2,2,3,3])