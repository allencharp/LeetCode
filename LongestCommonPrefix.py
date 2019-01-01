# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        zipped = zip(*strs)
        loc = 0
        for item in zipped:
            print(item)
            print(set(item))
            if len(set(item)) != 1:
                break
            else:
                loc = loc +1

        return strs[0][:loc]



s = Solution()
print(s.longestCommonPrefix(["str", "str1", "stl"]))