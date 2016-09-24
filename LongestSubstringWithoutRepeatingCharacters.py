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
			longest_str_set = longest_str_set | set(val)
			
			for i,v in enumerate(s[loc:]):
				if v in longest_str_set:
					break;
				else:
					longest_str_set |= set(v)