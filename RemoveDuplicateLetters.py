# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appear once and only once. You must make
# sure your result is the smallest in lexicographical order among all possible results.
#
# Example:
# Given "bcabc"
# Return "abc"
#
# Given "cbacdcbc"
# Return "acdb"

class Solution(object):
	def removeDuplicateLetters(self, s):

		rtnList = []

		for alph in s:
			if alph not in rtnList:
				rtnList.append(alph)

		rtnList.sort()

		return "".join(rtnList)

s = Solution()
print s.removeDuplicateLetters("cbacdcbc")
