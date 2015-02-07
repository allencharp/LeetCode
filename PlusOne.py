# Given a non-negative number represented as an array of digits, plus one to the number.
# 
# The digits are stored such that the most significant digit is at the head of the list.

class Solution:
	
	def __init__(self):
		self.requireAddOneFlag = False;
		self.firstAddOneFlag = True
	
	def handleDigit(self, i):
		if(i == 9):
			i = 0
			self.requireAddOneFlag = True;
		else:	
			i = i + 1
			self.requireAddOneFlag = False;
		return i;
	# @param digits, a list of integer digits
	# @return a list of integer digits
	def plusOne(self, digits):
		
		stack = []
		
		for i in digits[::-1]:
			
			if self.requireAddOneFlag:
				i = self.handleDigit(i)
				
			
			if(self.firstAddOneFlag):
				i = self.handleDigit(i)
				self.firstAddOneFlag = False
			
			stack.append(i)	
		
		if(self.requireAddOneFlag):
			stack.append(1);	
			
		rtnList = []
		l = len(stack)
		for i in range(l):
			rtnList.append(stack.pop())
		return rtnList
	
list = [1,0]
s = Solution()
print s.plusOne(list)