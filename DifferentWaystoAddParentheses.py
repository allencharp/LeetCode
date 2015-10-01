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

    def __init__(self):
        self.operator = ["+", "-", "*"]
        self.numList = []
        self.operList = []
        self.rtnDict = {} # {key, [value1, value2]}

    def diffWaysToCompute(self, input):

        self.getNumber(input)
        self.getOperator(input)

        numLen = len(self.numList)

        if(numLen == 0):
            return None

        for n in range(1, numLen+1):

            if n == 1:
                self.rtnDict[1] = []
                self.rtnDict[1].append((int)(self.numList[0]))

            elif n == 2:
                num1 = self.numList[0]
                num2 = self.numList[1]
                operator = self.operList[0]
                self.rtnDict[2] = []
                self.rtnDict[2].append(self.getResult(num1, num2, operator))

            else:
                thisNum = self.numList[n - 1]
                lastNum = self.numList[n - 2]
                thisOperator = self.operList[n - 1 - 1]
                lastOperator = self.operList[n - 1 - 2]

                self.rtnDict[n] = []

                # catalan number
                # this number +-* last time possibilities
                for i in (self.rtnDict[n-1]):

                    self.rtnDict[n].append(self.getResult(i, thisNum, thisOperator))

                thisResult = self.getResult(lastNum, thisNum, thisOperator)
                for i in self.rtnDict[n-2]:
                    self.rtnDict[n].append(self.getResult(i, thisResult, lastOperator))


        return self.rtnDict[numLen]


    def getResult(self, num1str, num2str, operator):
        num1 = (int)(num1str)
        num2 = (int)(num2str)

        if(operator == "+"):
            return num1 + num2
        elif(operator == "*"):
            return num1 * num2
        else:
            return num1-num2

    def getNumber(self, input):
        import re
        self.numList = re.split("\-|\+|\*", input)
        #return self.numList

    def getOperator(self, input):
        for i in range(len(input)):
            if input[i] == "+" or input[i] == "-" or input[i] == "*":
                self.operList.append(input[i])
    #
    # def catalan_number(n):
    #     nm = dm = 1
    #     for k in range(2, n+1):
    #       nm, dm = ( nm*(n+k), dm*k )
    #     return nm/dm

s = Solution()
print s.diffWaysToCompute("2*3-4*5")
print s.rtnDict

