# Given an input string, reverse the string word by word.
# 
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

class Solution:
	# @param s, a string
	# @return a string
	def reverseWords(self, s):
		rtnValue = ""
		
		array = s.split(' ')
		for i in range(len(array))[::-1]:
			if(len(array[i]) >= 1):
				rtnValue = rtnValue + array[i] + " "
			
		return rtnValue.strip()
		

s = Solution()
s.reverseWords(" ")
