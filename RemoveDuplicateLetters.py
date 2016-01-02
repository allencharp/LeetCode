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

		start,loc = self.whereToStart(0, s)
		rtnList.append(start)

		while loc < len(s):
			loc2 = loc
			(start,loc) = self.whereToStart(loc, s)
			if loc == loc2:
				break;

			rtnList.append(start)

		# what is lexicographical order ?
		# https://en.wikipedia.org/wiki/Lexicographical_order
		# e.g. a < aa < aaa < ab < abb < abc < b < bcd < be < ...

		return "".join(rtnList)

	def whereToStart(self, froms, s):
		wheretostart = s[froms]
		where = froms
		for loc in range(froms, len(s)):
			cur = s[loc]

			if cur < wheretostart and self.isContains(self.getDistinctList(s[0:loc]), self.getDistinctList(s[loc:len(s)])):
				wheretostart = cur
				where = loc
		return (wheretostart, where)

	def getDistinctList(self, s):
		rtnList = []
		for item in s:
			if item not in rtnList:
				rtnList.append(item)
		return rtnList

	def isContains(self, frontList, rearList):
		return True

# s = Solution()
# print s.removeDuplicateLetters("bcabc")
list1 = [1,2]
list2 = [2,3,1]
print list2.