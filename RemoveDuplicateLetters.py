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
import collections

class Solution(object):
	def removeDuplicateLetters(self, s):
		ans = ''
		for x in range(len(set(s))):
			top, idx = s[0], 0
			counter = collections.Counter(s)
			for y in range(len(s)):
				if top > s[y]:
					top, idx = s[y], y
				if counter[s[y]] == 1:
					break
				counter[s[y]] -= 1
			ans += top
			s = s[idx+1:].replace(top,'')
		return ans
		# rtnList = []
		#
		# for i in range(len(s)-1, 0, -1):
		# 	alph = s[i]
		# 	if alph not in rtnList:
		# 		rtnList.append(alph)
		#
		# # what is lexicographical order ?
		# # https://en.wikipedia.org/wiki/Lexicographical_order
		# # e.g. a < aa < aaa < ab < abb < abc < b < bcd < be < ...
		# rtnList.reverse()
		#
		# return "".join(rtnList)

s = Solution()
print s.removeDuplicateLetters("cbacdcbc")
