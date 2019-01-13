# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
# Output: 2
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_nums = [i for i in range(len(nums)+1)]
        print(list_nums)
        for i,v in enumerate(nums):
            list_nums.remove(v)

        print(list_nums[0])
        return list_nums[0]


s = Solution()
print(s.missingNumber([3,0,2,4,7,5,6,8]))

