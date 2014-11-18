#Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

#For example,
#Given [100, 4, 200, 1, 3, 2],
#The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

#Your algorithm should run in O(n) complexity.
####################################################################################

# The key point of my solution to this algorithm is to use radix way to sort the num list
# After the sorting, we put the number into a stack and finally get the correct return value

class Solution:

	# 10 lists   -  0  1  2  3  4  5  6  7  8  9
	container = [[],[],[],[],[],[],[],[],[],[],[]]

	number = []
	def longestConsecutive(self, num):
		 
		self.number = num

		# loc = 1
		
		# maxDigit = self.GetMaxDigit(num)
		 
		# while(loc <= maxDigit):		 	
		# 	self.ArrageContainer(loc)
		# 	self.ResetNumberList();

		# 	loc = loc + 1

		# self.HandleNegative();
		self.number.sort()

		return self.GetSequence()

	def GetSequence(self):
		
		stack = []

		rtn = 1

		temp = 1
		
		for i in range(len(self.number)):
							
			item = self.number[i]

			if(len(stack) == 0):					
				stack.append(item)
			else:
				latest = stack.pop()
				if(item == latest + 1):
					stack.append(latest)
					stack.append(item)
					temp = temp + 1
					if(temp > rtn):
						rtn = temp
				elif(item == latest):
					stack.append(latest)
					pass
				else:
					stack = []
					
					temp = 1
					stack.append(item)
					
		return rtn

	# def GetMaxDigit(self, array):
	# 	max = 1
		
	# 	for item in array:
	# 		if( item < 0):
	# 			item = 0 - item

	# 		# Get the max digit of single number
	# 		i = len(str(item))

	# 		if(i > max):
	# 			max = i
				
	# 	return max

	

	# def ArrageContainer(self, loc):
	# 	self.container = [[],[],[],[],[],[],[],[],[],[],[]]
	# 	for item in self.number:
	# 		pos = item
	# 		if(item < 0):
	# 			pos = 0 - item;

	# 		digit = self.GetDigitFromLoc(pos, loc)

	# 		self.container[digit + 1].append(item)
	
	# # From right to left, get the specific location of 
	# # the digit number
	# def GetDigitFromLoc(self, number, loc):
	# 	number = number % (10 ** loc)
	# 	if(loc == 1):
	# 		return number
	# 	return (number / (10**(loc-1)))

	# def ResetNumberList(self):
	# 	self.number = []
	# 	for i in range(len(self.container)):
	# 		for j in range(len(self.container[i])):
	# 			item = self.container[i][j]
	# 			if(item is not None):
	# 				self.number.append(item)

	# def HandleNegative(self):

	# 	for i in range(len(self.number)):

	# 		single = self.number[i];

	# 		if(single < 0):
	# 			self.container[0].append(single)
		
	# 	for i in self.container[0]:
	# 		self.number.remove(i)
	# 	self.container[0].reverse()
		
	# 	self.number = self.container[0] + self.number
