# You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.
#
# Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.
#
# Example 1:
# Given x = [2, 1, 1, 2],

#
# Return true (self crossing)
# Example 2:
# Given x = [1, 2, 3, 4],

#
# Return false (not self crossing)
# Example 3:
# Given x = [1, 1, 1, 1],

#
# Return true (self crossing)
class Solution(object):
	def __init__(self):
		self.route = [(0,0)]
		self.currentX = 0
		self.currentY = 0

	def isSelfCrossing(self, x):

		if(len(x) < 4):
			return False

		for key in range(len(x)):
			val = x[key]
			if key % 4 == 0:
				for i in range((val)):
					self.currentY = self.currentY + 1
					if (self.currentX, self.currentY) in self.route:
						return True;
					else:
						self.route.append((self.currentX, self.currentY))
			elif key % 4 == 1:
				for i in range((val)):
					self.currentX = self.currentX - 1
					if (self.currentX, self.currentY) in self.route:
						return True;
					else:
						self.route.append((self.currentX, self.currentY))
			elif key % 4 == 2:
				for i in range((val)):
					self.currentY = self.currentY - 1
					if (self.currentX, self.currentY) in self.route:
						return True;
					else:
						self.route.append((self.currentX, self.currentY))
			else:
				for i in range((val)):
					self.currentX = self.currentX + 1
					if (self.currentX, self.currentY) in self.route:
						return True;
					else:
						self.route.append((self.currentX, self.currentY))
		return False

s = Solution()
print s.isSelfCrossing([2,1,1,2])