# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
class Solution(object):
    def calculate(self, s):
        s = s.strip().replace(" ", "")

        items = self.__splitCal(s)

        will_cal = False
        oper_without_backet_stack = []
        for chara in items:
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
            for i, v in enumerate(oper_without_backet_stack):
                if i == 0:
                    res = int(v)
                if v == "+":
                    res = res + int(oper_without_backet_stack[i + 1])
                if v == "-":
                    res = res - int(oper_without_backet_stack[i + 1])
            return int(res)
        else:
            return int(oper_without_backet_stack[0])

    def __splitCal(self, s):
        rtn_list = []
        temp_val = ""
        for item in s:

            if item in ['+', '-', '*', '/', '(', ')']:
                if temp_val != "":
                    rtn_list.append(temp_val)
                    temp_val = ""
                rtn_list.append(item)
            else:
                temp_val = temp_val + item

        if temp_val != "":
            rtn_list.append(temp_val)

        return rtn_list;
s = Solution()
print s.calculate("42")