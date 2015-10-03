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

        self.rtnDict = {} # {key, [value1, value2]}

    def diffWaysToCompute(self, input):

        numList = self.getNumber(input)
        operList = self.getOperator(input)

        num = len(numList)

        if num == 0:
            return None
        elif num == 1:
            self.rtnDict[numList[0]] = []
            self.rtnDict[numList[0]].append((int)(numList[0]))
        elif num == 2:
            num1 = numList[0]
            num2 = numList[1]
            operator = operList[0]
            self.rtnDict[num1+operator+num2] = []
            self.rtnDict[num1+operator+num2].append(self.getResult(num1, num2, operator))
        elif num >= 3:
            self.rtnDict[input] = []
            for i in range(1, len(numList)):
                startInput = self.getThisInput(numList, operList, 0, i - 1)
                endInput = self.getThisInput(numList, operList, i, len(numList) - 1)
                for startNum in self.diffWaysToCompute(startInput):
                    for endNum in self.diffWaysToCompute(endInput):
                        self.rtnDict[input].append(self.getResult(startNum, endNum, operList[i-1]))

        return self.rtnDict[input]

    def getThisInput(self, numList, operList, start, end):
        rtn = numList[start]
        for i in range(start, end):
            rtn = "{0}{1}{2}".format(rtn , operList[i] , numList[i+1])
        return rtn

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
        return re.split("\-|\+|\*", input)
        #return self.numList

    def getOperator(self, input):
        operList = []
        for i in range(len(input)):
            if input[i] == "+" or input[i] == "-" or input[i] == "*":
                operList.append(input[i])
        return operList

s = Solution()
print s.diffWaysToCompute("2*3-4*5-1")
print s.rtnDict


