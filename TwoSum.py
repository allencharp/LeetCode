# Given an array of integers, find two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they add up to the 
# target, where index1 must be less than index2. Please note that your returned answers 
# (both index1 and index2) are not zero-based.
# 
# You may assume that each input would have exactly one solution.
# 
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

		
class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		dict = {}
		for i in range(len(num)):
			if num[i] in dict:
				dict[num[i]].append(i+1)
			else:
				dict[num[i]] = [i+1]

		for i in range(len(num)):
			
			rest = target - num[i]
			
			if(num[i] == rest):
				if(len(dict[num[i]]) > 1):
					return dict[num[i]][0], dict[num[i]][1]
			
			elif((target - num[i]) in dict):
				return min(dict[target - num[i]][0], dict[num[i]][0]), \
						max(dict[target - num[i]][0], dict[num[i]][0])

		return ()

s = Solution()
a = [3,2,4,5]
print(s.twoSum(a,6))