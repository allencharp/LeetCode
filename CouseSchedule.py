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



class Solution:	
	# @param {integer} numCourses
	# @param {integer[][]} prerequisites
	# @return {boolean}
	def canFinish(self, numCourses, prerequisites):
		storeList = [];
		for i in range(numCourses):
			temp = []
			storeList.append(temp)

		for courses in prerequisites:
			if len(courses) > numCourses:
				return
			self.analysisCourse(storeList,numCourses, courses)	

	def analysisCourse(self, storelist, total, courses):
		for index,item in enumerate(courses):
			if not self.ExistInStoreList(storelist, item):
				(f, t) = self.GetRange(storelist, len(courses), index)

	def ExistInStoreList(self, storelist, course):
		for i, items in enumerate(storelist):
			if(course in items):
				return True
		return False

	def GetRange(self, storelist, len, index):
		pass

s = Solution()
temp = [[1,2,3],[1,4,5],[1,2,4],[1,5]]
print s.canFinish(5, temp)