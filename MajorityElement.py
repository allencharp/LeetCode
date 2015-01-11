# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than  n/2 times.
# 
# You may assume that the array is non-empty and the majority element always exist in the array.
class Solution:
	def __init__(self):
		self.dict = {}
	# @param num, a list of integers
	# @return an integer
	def majorityElement(self, num):
		for i in range(len(num)):
			curr = num[i]
			
			if(curr in self.dict):
				self.dict[curr] = self.dict[curr] + 1
			else:
				self.dict[curr] = 1
		for key in (self.dict):
			if(self.dict[key] > len(num)/2):
				return key
		
		
s = Solution()
print s.majorityElement([1,2,1,3,1])
