# Rotate an array of n elements to the right by k steps.

# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

# [show hint]

# Related problem: Reverse Words in a String II

# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.
class Solution:
	# @param nums, a list of integer
	# @param k, num of steps
	# @return nothing, please modify the nums list in-place.
	def rotate(self, nums, k):
		numsdict = {}
		for i in range(len(nums)):
			newLoc = i+k if i+k < len(nums) else (i+k)%len(nums)
			numsdict[newLoc] = nums[newLoc]	
			if i in numsdict:		
				nums[newLoc] = numsdict[i]
			else:
				nums[newLoc] = nums[i]
s = Solution()
num = [1,2,3]
s.rotate(num,1)
print num