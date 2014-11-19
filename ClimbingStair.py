class Solution:
    
    
    dict = {}
    
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n < 3:
            return n
        else:
            n1Key = n-1

            n1Value = 0;
            if(self.dict.has_key(n1Key)):
                n1Value = self.dict[n1Key]
            else:
                n1Value = self.climbStairs(n1Key)
                self.dict[n1Key] = n1Value
        
                n2Key = n-2

                n2Value = 0;
                if(self.dict.has_key(n2Key)):
                    n2Value = self.dict[n2Key]
                else:
                    n2Value = self.climbStairs(n2Key)
                    self.dict[n2Key] = n2Value
            return n1Value + n2Value
           
s = Solution()
print s.climbStairs(35)