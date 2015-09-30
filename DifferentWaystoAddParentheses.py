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

        n = len(self.numList)

        if n == 0:
            self.rtnDict[0] = []
            self.rtnDict[0].append(0)
            return self.rtnDict[0]
        elif(n == 1):
            self.rtnDict[1] = []
            self.rtnDict[1].append(self.numList[0])
            return self.rtnDict[1]
        elif(n == 2):
            num1 = self.numList[0]
            num2 = self.numList[1]
            operator = self.operList[0]
            self.rtnList[2] = []
            self.rtnList[2].append(self.getResult(num1, num2, operator))
            return self.rtnDict[2]
        else:
            numadd = self.numList[len(self.numList) - 1]
            numlast = self.numList[len(self.numList) - 2]



            pass


        """
        :type input: str
        :rtype: List[int]
        """
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
print s.diffWaysToCompute("2")
print s.rtnDict

