# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution(object):
	def reverse(self, x):
		strx = str(x)
		if strx[0] == '-':
			return int(strx[0]+(self.__reverseNum(strx[1:])))
		
		return int(self.__reverseNum(strx))
		
	
	def __reverseNum(self, x):
		lenx = len(x)
		rtn = ""
		for loc in range(len(x)):
			rtn = rtn + x[lenx-1-loc]
		return rtn


s = Solution()
print s.reverse(-123)