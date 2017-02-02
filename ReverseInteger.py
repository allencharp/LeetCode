# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
class Solution(object):
	def reverse(self, x):
		strx = str(x)
		retnVal = 0;
		if strx[0] == '-':
			retnVal = int(strx[0]+(self.__reverseNum(strx[1:])))
		
		else:
			retnVal = int(self.__reverseNum(strx))
		
		# overflow issue
		if retnVal >= 2**31-1 or retnVal <= -(2**31-1):
			retnVal = 0
		
		return retnVal
		
	
	def __reverseNum(self, x):
		lenx = len(x)
		rtn = ""
		for loc in range(len(x)):
			rtn = rtn + x[lenx-1-loc]
		return rtn


s = Solution()
print s.reverse(-123)