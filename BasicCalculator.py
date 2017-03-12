# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23

class Solution(object):
	def __init__(self):
		self.oper_with_backet_stack = []
		self.oper_without_backet_stack = []
	
	def calculate(self, s):
		pass
	
	def calculate_without_backet(self, s):
		will_cal = False
		
		for chara in s:
			self.oper_without_backet_stack.append(chara)
			
			if will_cal:
				left = self.oper_without_backet_stack.pop()
				oper = self.oper_without_backet_stack.pop()
				right = self.oper_without_backet_stack.pop()
				
				if oper == "*":
					res = int(left) * int(right)
				if oper == "/":
					res = int(left) / int(right)
					
				self.oper_without_backet_stack.append(res)
			
			if chara in ["*", "/"]:
				will_cal = True
		
		will_cal = False
		# now * and / should be removed
		for i,v in enumerate(self.oper_without_backet_stack):
			if v in ["+", "-"]:
				will_cal = True
			if will_cal:
				left = self.oper_without_backet_stack.pop()
				oper = self.oper_without_backet_stack.pop()
				right = self.oper_without_backet_stack.pop()
				
				if oper == "+":
					res = int(left) + int(right)
				if oper == "-":
					res = int(left) - int(right)
				
				return res


s = Solution()
print s.calculate_without_backet("1+5*2")
