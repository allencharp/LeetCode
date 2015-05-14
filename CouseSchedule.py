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
		rtn = True
		storeList = [];
		if not self.Seqence(prerequisites):
			return False
		
		for i in range(numCourses):
			temp = []
			storeList.append(temp)

		for courses in prerequisites:
			if len(courses) > numCourses:
				return
			rtn = self.analysisCourse(storeList,numCourses, courses)
			rtn  = self.checkResult(storeList, courses);
			if(rtn is False):
				break;
			
		return rtn
	
	def Seqence(self,courses):
		for i, items in enumerate(courses):
			for j,item in enumerate(items):
				if(j+1 <= len(items)-1):
					if items[j+1] <= item:
						return False
	
	def checkResult(self, storelist, courses):
		same = 0
		for items in storelist:
			if set(courses).issubset(set(items)):
				same = same + 1
		if(same == 1):
			return False
		return True

	def analysisCourse(self, storelist, total, courses):
		for index,item in enumerate(courses):
			if not self.ExistInStoreList(storelist, item):	
				(f, t) = self.GetRange(total, len(courses), index)
				self.Add(storelist, (f,t), item)
			else:
				(f1, t1) = self.GetExistingRange(storelist, item)
				(f2, t2) = self.GetRange(total,len(courses), index)
				if(t1 < f2):
					return False
				if (t2 < f1):
					return False

				self.Remove(storelist, (min(f1, f2), max(t1,t2)), item)
				self.Add(storelist, (max(f1, f2), min(t1,t2)), item)

		return True		

	def ExistInStoreList(self, storelist, course):
		for i, items in enumerate(storelist):
			if(course in items):
				return True
		return False

	def GetRange(self, total, len, index):
		f = index
		t = index + (total - len)
		return (f, t)

	def GetExistingRange(self, storelist, item):
		f=t = -1
		for i, items in enumerate(storelist):
			if(item in items):
				if(f == -1 or t == -1):
					f = i
					t = i
				else:
					t = t+1
		return (f,t)
	def Remove(self, storelist, area, item):
		(f,t) = area
		for temp in storelist[f:t+1]:
			if(item in temp):
				temp.remove(item)


	def Add(self, storelist, area, item):
		(f,t) = area
		for temp in storelist[f:t+1]:		
			temp.append(item)


s = Solution()
temp = [[1,2,3],[1,4,5],[1,2,4],[1.5]]
print s.canFinish(5, temp)