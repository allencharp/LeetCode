# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10 nn.
#
# Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100
# , excluding [11,22,33,44,55,66,77,88,99])

class Solution(object):
	def countNumbersWithUniqueDigits(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if len(str(n)) == 0:
			return 0
		elif len(str(n)) == 1:
			return 0
		elif len(str(n)) == 2:
			return 9
		else:
			pass