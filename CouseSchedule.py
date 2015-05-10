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
		storelist = []
		for i, courses in enumerate(prerequisites):
			for j, course in enumerate(courses):
				if(len(storelist) == 0):
					tempList = []
					tempList.append(course)
					storelist.append(tempList)
				else:
					
    		
