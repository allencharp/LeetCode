# __author__ = 'allen'
# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
#
#
# Example 1
# Input: "2-1-1".
#
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Output: [0, 2]
#
#
# Example 2
# Input: "2*3-4*5"
#
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10]

class Solution(object):
    #def Solution(self):
    operator = ["+", "-", "*"]
    numList = []
    operList = []

    def diffWaysToCompute(self, input):

        self.getNumber(input)
        self.getOperator(input)


        """
        :type input: str
        :rtype: List[int]
        """
        pass
    def getNumber(self, input):
        import re
        self.numList = re.split("\-|\+|\*", input)
        #return self.numList

    def getOperator(self, input):
        for i in range(len(input)):
            if input[i] == "+" or input[i] == "-" or input[i] == "*":
                self.operList.append(input[i])


    def catalan_number(n):
        nm = dm = 1
        for k in range(2, n+1):
          nm, dm = ( nm*(n+k), dm*k )
        return nm/dm

s = Solution()
s.diffWaysToCompute("2*3-4*5")
print s.operList
