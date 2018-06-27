# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
class Solution(object):

    def permute(self, nums):

        return_list = []

        for i,v in enumerate(nums):
            if i == 0:
                return_list.append([v])
                continue

            temp_every_time_list = []
            for itemList in return_list:
                for index,value in enumerate(itemList):
                    temp_every_time_list.append(itemList[0:index] + [v] + itemList[index:])
                temp_every_time_list.append(itemList + [v]) # add the last one
            return_list = temp_every_time_list

        return return_list





itemList = ["a","b","c"]
# temp_every_time_list = []
# v = "d"
# for index, value in enumerate(itemList):
#     temp_every_time_list.append(itemList[0:index] + [v] + itemList[index:])
# print(temp_every_time_list)

s = Solution()
print(s.permute(itemList))
