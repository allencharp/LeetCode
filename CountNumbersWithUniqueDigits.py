# Given a non-negative integer n, count all numbers with unique digits, x, where 0 <= x < 10**n.
#
# Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range of 0 <= x < 100
# , excluding [11,22,33,44,55,66,77,88,99])
739
class Solution(object):
	def countNumbersWithUniqueDigits(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		return 10**n - self.countNumberWithMultiDigits(n)

	def countNumberWithMultiDigits(self, n):
		if n == 0:
			return 0
		elif n == 1:
			return 0
		elif n == 2:
			return 9
		else:
			last_time = self.countNumberWithMultiDigits(n-1)
			return last_time + ((self.getNum(n-1, True) + 9 * self.getNum(n-1)) * 9)
	
	def getNum(self, sum, incl_first = False):
		rtn = 0
		for i in range(1, sum+1):
			if not incl_first and i == 1:
				continue
				
			rtn += 9 ** (sum - i) * self.getCNum(sum, i)
		
		return rtn
	
	def getCNum(self, sum, n):
		mother = 1
		sun = 1
		
		for i in range(sum-n+1, sum+1):
			sun *= i
		for i in range(1,n+1):
			mother *= i
		return sun/mother

s = Solution()
print s.countNumbersWithUniqueDigits(4)
#print s.countNumbersWithUniqueDigits(3)

# 3- 739
# 4 - 5275
