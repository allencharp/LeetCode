# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# 
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
# 
# Note: 
# You may assume k is always valid, 1 <= k <= array's length.
# 
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.
class Solution:
	# @param {integer[]} nums
	# @param {integer} k
	# @return {integer}
	def findKthLargest(self, nums, k):
		s = sorted(nums, reverse=True)
		
		return s[k-1]


t = [1,5,4,3,2]

s = Solution()
print s.findKthLargest(t, 2)