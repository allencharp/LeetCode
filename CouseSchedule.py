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
	def UpdateStoreList(self, storelist, courses):
		tempList = []
		for i,course in enumerate(courses):			
			temp = TempCourse()
			temp.course = course
			newIndex = 0
			where = self.ExistInStoreList(storelist, course)
			
			if(where is -1):
				newIndex = self.MoveInStoreList(storelist, tempList, course)
			else:
				newIndex = self.RefreshCousesList(storelist, tempList, course,where, i)

			temp.originLoc = i
			temp.newLoc = newIndex
			tempList.append(temp)
			if not self.IsSuccess(tempList):
				return False
		return True;

	
	def ExistInStoreList(self, storelist, course):
		for i, items in enumerate(storelist):
			if(course in items):
				return i
		return -1

	def MoveInStoreList(self, storelist, tempList,course):
		if len(storelist) == 0: #or len(tempList) == 0:
			temp = []
			temp.append(course)
			storelist.append(temp)
			return 0
		elif len(tempList) == 0:
			storelist[0].append(course)
			return 0
		elif (len(storelist) <= tempList[len(tempList)-1].newLoc + 1):
			temp = []
			temp.append(course)
			storelist.append(temp)
			return len(storelist)-1
		else:
			storelist[tempList[len(tempList)-1].newLoc + 1].append(course)
			return tempList[len(tempList)-1].newLoc + 1

	def RefreshCousesList(self, storelist,tempList, course, where, currentIndex):
		if(len(tempList) == 0):
			return where
		elif where == tempList[currentIndex-1].newLoc:
			storelist[where].remove(course)
			if(len(storelist)-1 == where):
				temp = []
				temp.append(course)
				storelist.append(temp)
			else:
				storelist[where+1].append(course)
			return where + 1
		else:
			return where

	def IsSuccess(self, tempList):
		for i,temp in enumerate(tempList):
			cur = temp.newLoc;
			for j in range(i,len(tempList)):
				nex = tempList[j].newLoc
				if(cur > nex):
					return False
		return True


s = Solution()
temp = [[1,2,3],[1,4,5],[1,2,4],[1,]]
print s.canFinish(5, temp)