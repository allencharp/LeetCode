# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6



class Solution(object):
    def maxSubArray(self, nums):

        max = 0

        if not nums:
            return 0

        for index1 in range(len(nums)):
            for index2 in range(index1, len(nums)):
                if max < sum(nums[index1: index1+index2]):
                    max = sum(nums[index1: index1+index2])
                    print(max)

        return max



s = Solution()
print(s.maxSubArray([4,-1,2,1]))