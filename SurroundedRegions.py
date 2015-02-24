# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# 
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
# 
# X X X X
# X X X X
# X X X X
# X O X X

class Solution:
	def __init__(self):
		self.alivelist = []
		
		self.currentStackAlive = False
		self.currentStack = [] 
		
		self.b = None
	# @param board, a 2D array
	# Capture all regions by modifying the input board in-place.
	# Do not return any value.
	def solve(self, board):
		self.b = board
		for i in range(len(board)):
			for j in range(len(board[i])):
				if(board[i][j] == 'O' and self.IsSearched((i,j)) is False):
					self.currentStackAlive = False
					self.AnalysisO((i,j))
					
					if(self.currentStackAlive is False):
						self.ChangeOToX()
					else:
						self.PutToAliveList()
						
					self.currentStack = []
					
		board = self.b
	
	def IsSearched(self, loc):
		if((loc in self.alivelist) or (loc in self.currentStack)):
			return True
		return False
	
	def AnalysisO(self, loc):
		(i,j) = loc
		if(self.IsWall(loc) is False and self.IsSearched(loc) is False):
			self.currentStack.append(loc)
			if(self.IsUpSurrend(loc) is False):
				self.AnalysisO((i-1,j))
			elif(self.IsDownSurrend(loc) is False):
				self.AnalysisO((i+1, j))
			elif(self.IsLeftSurrend(loc) is False):
				self.AnalysisO((i, j-1))
			elif(self.IsRightSurrend(loc) is False):
				self.AnalysisO((i, j+1))
		elif(self.IsWall(loc) and self.b[i][j] == 'O'):
			self.currentStackAlive = True
			
	def IsUpSurrend(self, loc):
		(i,j) = loc
		return self.IsSurrend((i-1,j))
	
	def IsLeftSurrend(self, loc):
		(i,j) = loc
		return self.IsSurrend((i,j-1))
	
	def IsRightSurrend(self, loc):
		(i,j) = loc
		return self.IsSurrend((i,j+1))
	
	def IsDownSurrend(self, loc):
		(i,j) = loc
		return self.IsSurrend((i+1,j))
	
	def IsSurrend(self, loc):
		(i,j) = loc
		if(self.b[i][j] == 'X'):
			return True
		return False
	
	def IsWall(self, loc):
		(i,j) = loc;
		if(i == len(self.b) - 1 or j == len(self.b[i]) - 1):
			return True
		return False;
	
	def ChangeOToX(self):
		for item in range(len(self.currentStack)):
			(i,j) = self.currentStack[item]
			self.b[i][j] = 'X'
		
	def PutToAliveList(self):
		self.alivelist.append(self.currentStack)
	
	
board = [
		['X','X','X','X','X','X'],
		['X','O','O','X','O','O'],
		['X','X','X','X','X','X']
		]
s = Solution()
s.solve(board)
print board