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
		self.searchlist = {}
		self.b = None
	# @param board, a 2D array
	# Capture all regions by modifying the input board in-place.
	# Do not return any value.
	def solve(self, board):
		self.b = board
		for i in range(board):
			for j in range(board[i]):
				if(board[i][j] == 'O' and self.IsSearched((i,j)) is False):
					self.AnalysisO((i,j))
	
	def IsSearched(self, loc):
		if(loc in self.searchlist):
			return True
		return False
	
	def AnalysisO(self, loc):
		(i,j) = loc
		if(self.IsWall(loc) is False):
			pass
	def IsUpSurrend(self, loc):
		pass
	def IsLeftSurrend(self, loc):
		pass
	def IsRightSurrend(self, loc):
		pass
	def IsDownSurrend(self, loc):
		pass
	def IsWall(self, loc):
		(i,j) = loc;
		if(i == len(self.b) -1 or j == len(self.b[i]) - 1):
			return True
		return False;