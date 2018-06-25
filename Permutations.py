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

        temp_list = []

        for i,v in enumerate(nums):
            temp_every_time_list = []
            for itemList in temp_list:
                for index,value in enumerate(itemList):
                    temp_every_time_list.append(itemList[index:len(itemList)] + [v] + itemList[index:])
                temp_every_time_list.append(itemList + [v])



temp = ["a","b","c"]
v = "d"
temp_list = []
temp_list.append(temp+[v])
for index,value in enumerate(temp):
    temp_list.append(temp[0:index] + [v] + temp[index:])
print(temp_list)
