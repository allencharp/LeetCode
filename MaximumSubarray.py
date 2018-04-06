# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6



class Solution(object):
    def maxSubArray(self, nums):

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        max = min(nums)

        for index1 in range(len(nums)):
            if nums[index1] <= 0 and max > 0:
                continue
            for index2 in range(index1, len(nums)+1):

                if nums[index1: index2+1] and max < sum(nums[index1: index2+1]):
                    max = sum(nums[index1: index2+1])


        return max


s = Solution()
print(s.maxSubArray([-2,0,-1]))