# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Subscribe to see which companies asked this question

class Solution(object):
	def lengthOfLongestSubstring(self, s):
		
		if len(s) <= 1:
			return len(s)
		for loc, val in enumerate(s):
				for i in s[loc:]:
					pass