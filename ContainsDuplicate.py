# Given an array of integers, find if the array contains any duplicates. 
# Your function should return true if any value appears at least twice in the array, 
# and it should return false if every element is distinct.

class Solution:
	# @param {integer[]} nums
	# @return {boolean}
	def containsDuplicate(self, nums):
		dict = {}
		for i,num in enumerate(nums):
			if num in dict:
				return True
			else:
				dict[num]=i
		return False

list = [1,2,2]
s = Solution();
print s.containsDuplicate(list)