# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
class Solution(object):
    def moveZeroes(self, nums):

        if len(nums) == 0 or len(nums) == 1:
            return nums

        for loc in range(len(nums)):
            if(nums[loc] == 0 and loc != len(nums) - 1):
                self.moveZeroToLast(loc, nums)
        return nums


    def moveZeroToLast(self, loc, nums):
        for i in range(loc, len(nums)-1):
            nums[i], nums[i+1] = nums[i+1], nums[i]


s = Solution()
print s.moveZeroes([0,0,1])


