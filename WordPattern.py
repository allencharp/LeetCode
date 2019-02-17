# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
#
# Example 1:
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# Example 2:
#
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# Example 3:
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# Example 4:
#
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict = {}
        input_str_list = str.split(' ')
        print(input_str_list)
        if len(pattern) != len(input_str_list):
            return False
        for p_i,p_v in enumerate(pattern):
            if p_v in dict.keys():
                if dict[p_v] != input_str_list[p_i]:
                    return False
            else:
                if input_str_list[p_i] in dict.values():
                    return False
                dict[p_v] = input_str_list[p_i]
        return True




s = Solution()
print(s.wordPattern("abba","cat cat cat cat"))