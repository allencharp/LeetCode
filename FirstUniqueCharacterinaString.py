# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.
class Solution(object):
	
	def __init__(self):
		self.repeatLocList = []
	
	def firstUniqChar(self, s):
		
		if len(s) == 0:
			return -1
		
		for loc, value in enumerate(s):
			is_repeat = False
			if loc not in self.repeatLocList:
				for l, v in enumerate(s[loc+1::]):
					if v == value:
						self.repeatLocList.append(loc+l+1)
						is_repeat = True
			if not is_repeat and loc not in self.repeatLocList:
				return loc
		return -1
			
s = "cc"
solution = Solution()
print solution.firstUniqChar(s)