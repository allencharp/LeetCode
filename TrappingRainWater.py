# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it is able to trap after raining.
# 
# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

class Solution:
	
	
	# @param A, a list of integers
	# @return an integer
	def trap(self, A):
		uTrapper = []
		
		i = 0
		leftIndex = 0
		rightIndex = 0
		# only 2 left could not trap water
		while (i < (len(A) - 2)):
			leftIndex = self.findLeftBank((A[i:])) + i
			
			rightIndex = self.findRightBank((A[leftIndex+1:]), A[leftIndex]) + leftIndex + 1
					
			uTrapper.append((A[leftIndex : rightIndex+1]))
			i = rightIndex
		
		return self.getRainWater(uTrapper)
			
	def findLeftBank(self, list):
		for i in range(len(list)):
			curr = list[i]
			currNext = list[i+1] if i+1 < len(list) else 0
			
			if(curr > currNext):
				return i
		return len(list) - 1
		
	def findRightBank(self, list, leftHight):
		biggestLoc = len(list)
		biggest = 0
		for i in range(len(list)):
			if(list[i] >= leftHight):
				return i
			if(list[i] > biggest):
				biggestLoc = i
				biggest = list[i]
				
		return biggestLoc
		
	def getRainWater(self, lists):

		all = 0
		for i in range(len(lists)):
			list = lists[i]
			
			height = min(list[0], list[len(list)-1])
			for i in range(1, len(list)-1):
				if(list[i] > height):
					continue
				all = all + (height - list[i])
		return all

s = Solution()
print s.trap([9,6,8,8,5,6,3])
