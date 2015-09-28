#Given an integer, write a function to determine if it is a power of two.

class Solution(object):
    def isPowerOfTwo(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		if(n==1 or n==2):
			return True
		result = n
		while(result/2 != 0):
			pos = result % 2
			result = result / 2


			if(result == 2 and pos == 0):
				return True

			if(pos == 1):
				break;

		return False

s = Solution()
print s.isPowerOfTwo(5)