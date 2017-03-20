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
	
	def calculate(self, s):
		
		s = s.strip().replace(" ","")

		items = self.__splitCal(s)

		for v in items:
			self.oper_with_backet_stack.append(v)
			
			if v == ")":
				back_str = self.__get_backet_list();
				back_val = self.calculate_without_backet(back_str)
				self.oper_with_backet_stack.append(back_val)
				
				
		if len(self.oper_with_backet_stack) != 1:
			fin_val = self.__get_backet_list()
			return (int)(self.calculate_without_backet(fin_val));
		else:
			return (int)(self.oper_with_backet_stack[0]);


	def __splitCal(self,s):
		rtn_list = []
		temp_val = ""
		for item in s:

			if item in ['+','-','*','/','(',')']:
				if temp_val != "":
					rtn_list.append(temp_val)
					temp_val = ""
				rtn_list.append(item)
			else:
				temp_val = temp_val+item

		if temp_val != "":
			rtn_list.append(temp_val)

		return rtn_list;

	def calculate_without_backet(self, s):
		will_cal = False
		oper_without_backet_stack = []
		for chara in s:
			oper_without_backet_stack.append(chara)
			
			if will_cal:
				second = oper_without_backet_stack.pop()
				oper = oper_without_backet_stack.pop()
				first = oper_without_backet_stack.pop()
				
				if oper == "*":
					res = int(first) * int(second)
				if oper == "/":
					res = int(first) / int(second)
					
				oper_without_backet_stack.append(res)
				
				will_cal = False
				
			if chara in ["*", "/"]:
				will_cal = True
		
		res = 0
		
		if len(oper_without_backet_stack) != 1:
			# now * and / should be removed
			for i,v in enumerate(oper_without_backet_stack):
				if i == 0:
					res = int(v)
				if v == "+":
					res = res + int(oper_without_backet_stack[i + 1])
				if v == "-":
					res = res - int(oper_without_backet_stack[i + 1])
			return res
		else:
			return oper_without_backet_stack[0]

	def __get_backet_list(self):
		
		# )
		if self.oper_with_backet_stack[len(self.oper_with_backet_stack)-1] == ")":
			self.oper_with_backet_stack.pop()
			
		rtn_val_list = []
		
		v = self.oper_with_backet_stack.pop()
		while v != "(" :
			rtn_val_list.append(str(v))
			v = self.oper_with_backet_stack.pop()
			if len(self.oper_with_backet_stack) == 0 and v != "(":
				rtn_val_list.append((v))
				break;
				
		return reversed(rtn_val_list)

s = Solution()
print s.calculate(" ( 32 +1)")
