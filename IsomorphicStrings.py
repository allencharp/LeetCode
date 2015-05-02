# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# For example,
# Given "egg", "add", return true.

# Given "foo", "bar", return false.

# Given "paper", "title", return true.

# Note:
# You may assume both s and t have the same length.

class Solution:
	def __init__(self):
		self.sdict = {}
		self.tdict = {}
	# @param {string} s
	# @param {string} t
	# @return {boolean}
	def isIsomorphic(self, s, t):
		if (len(s) != len(t)):
			return False;

		for (sLoc, tLoc) in zip(range(len(s)),range(len(t))):
			sChar = s[sLoc]
			tChar = t[tLoc]
			if (not (sChar in self.sdict) and (not (tChar in self.tdict))):
				self.sdict[sChar] = sLoc
				self.tdict[tChar] = tLoc
			elif(sChar in self.sdict and tChar in self.tdict):
				if(self.sdict[sChar] != self.tdict[tChar]):
					return False;
				self.sdict[sChar] = sLoc
				self.tdict[tChar] = tLoc
			else:
				return False

		return True


s = "aba"
t = "baa"
solu = Solution()
print solu.isIsomorphic(s, t)
