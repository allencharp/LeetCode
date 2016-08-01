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
			return last_time + ((10 * (n-1) - 1 + 9) * 9 )



s = Solution()
print s.countNumbersWithUniqueDigits(3)

# 3- 739
# 4 - 5275
