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

		for i in range(len(s)):
			alph = s[i]
			if alph not in rtnList:
				rtnList.append(alph)
			else:
				if(len(rtnList) == 0):
					continue;

				for loc, val in enumerate(rtnList):
					if val == alph and loc != len(rtnList) - 1:

						if(rtnList[loc+1] < val):
							rtnList.remove(val)
							rtnList.append(val)

		# what is lexicographical order ?
		# https://en.wikipedia.org/wiki/Lexicographical_order
		# e.g. a < aa < aaa < ab < abb < abc < b < bcd < be < ...

		return "".join(rtnList)

s = Solution()
print s.removeDuplicateLetters("bcabc")
