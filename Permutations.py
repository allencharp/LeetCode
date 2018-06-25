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

        temp_list = []

        for i,v in enumerate(nums):
            if i == 0:
                temp_list.append([v])
                continue

            temp_every_time_list = []
            for itemList in temp_list:
                for index,value in enumerate(itemList):
                    if i == 0:
                        temp_every_time_list.append([v] + [value])
                        continue
                    temp_every_time_list.append(itemList[index:len(itemList)] + [v] + itemList[index:])
                temp_every_time_list.append(itemList + [v])
            temp_list = temp_every_time_list

        return temp_list





temp = ["a","b","c"]

s = Solution()
print(s.permute(temp))
