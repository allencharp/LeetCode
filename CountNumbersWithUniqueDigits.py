# Given a non-negative integer n, count all numbers with unique digits, x, where 0 <= x < 10**n.
#
# Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range of 0 <= x < 100
# , excluding [11,22,33,44,55,66,77,88,99])
class Solution(object):
	def countNumbersWithUniqueDigits(self, n):
		if n == 0:
			return 1
		elif n == 1:
			return 10
		elif n == 2:
			return 91
		else:
			last_time = self.countNumbersWithUniqueDigits(n-1)
			return last_time + self.getComposeNum(n-1)*9
		
	def getComposeNum(self, sum):
		start = 9
		rtn = 1
		for i in range(sum):
			rtn *= start
			start -= 1
		return rtn
		

s = Solution()
print s.countNumbersWithUniqueDigits(5)
print s.getComposeNum(2)
#print s.getCNum(3,1)
# 3- 739
# 4 - 5275
# 5 - 32491
