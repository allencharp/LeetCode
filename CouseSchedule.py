# There are a total of n courses you have to take, labeled from 0 to n - 1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
# which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# For example:

# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, 
# and to take course 0 you should also have finished course 1. So it is impossible.

class TempCourse:
	def __init__(self):
		originLoc = 0;
		newLoc = 0;
		course = ""

class Solution:	
	tempList = []
	# @param {integer} numCourses
	# @param {integer[][]} prerequisites
	# @return {boolean}
	def canFinish(self, numCourses, prerequisites):
		coursestorelist = []
		for courses in (prerequisites):
			issucceed = self.UpdateStoreList(coursestorelist, courses)
			if not issucceed:
				return False
		return True			
	# @param {storeList} 
	def UpdateStoreList(self, storeList, courses):
		
		for i,course in enumerate(courses):			
			temp = TempCourse()
			temp.course = course
			if(self.ExistInStoreList(storeList, course) is not -1):
				newIndex = self.MoveInStoreList(storelist, self.tempList)
			else:
				newIndex = self.RefreshCousesList(storelist, self.tempList, course)
			temp.originLoc = i
			temp.newLoc = newIndex
			self.tempList.append(temp)
			if not self.IsSuccess(self.tempList):
				return False
		return True;

	
	def ExistInStoreList(self, storeList, course):
		for i, items in storelist:
			if(course in storelist):
				return i
		return -1

	def MoveInStoreList(self, storeList):
		if len(storelist) == 0:
			return 0
		else:
			return storeList[len(storelist)-1].newLoc + 1

	def RefreshCousesList(self, storelist, course):
		pass
	def IsSuccess(self, couseList):
		pass