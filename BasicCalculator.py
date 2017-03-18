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
		
		for v in s:
			self.oper_with_backet_stack.append(v)
			
			if v == ")":
				back_str = self.__get_backet_string();
				back_val = self.calculate_without_backet(back_str)
				self.oper_with_backet_stack.append(back_val)
				
		fin_val = self.__get_backet_string()
		return self.calculate_without_backet(fin_val);
	
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
				
				will_cal = False
				
			if chara in ["*", "/"]:
				will_cal = True
		
		res = 0
		
		if len(self.oper_without_backet_stack) != 1:
			# now * and / should be removed
			for i,v in enumerate(self.oper_without_backet_stack):
				if i == 0:
					res = int(v)
				if v == "+":
					res = res + int(self.oper_without_backet_stack[i + 1])
				if v == "-":
					res = res = int(self.oper_without_backet_stack[i + 1])
			return res
		else:
			return self.oper_without_backet_stack[0]

	def __get_backet_string(self):
		
		# )
		if self.oper_with_backet_stack[len(self.oper_with_backet_stack)-1] == ")":
			self.oper_with_backet_stack.pop()
		
		rtn_val = ""
		
		v = self.oper_with_backet_stack.pop()
		while v != "(" and len(self.oper_with_backet_stack) != 0:
			rtn_val = rtn_val + str(v)
			v = self.oper_with_backet_stack.pop()
		return rtn_val

s = Solution()
print s.calculate("(1+(4+5+2)-3)+(6+8)")
