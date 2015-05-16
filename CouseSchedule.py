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
		degrees = [0] * numCourses
		parents = [[] for x in range(numCourses)]
		for pair in prerequisites:
			degrees[pair[1]] += 1
			parents[pair[0]].append(pair[1])
		courses = set(range(numCourses))
		flag = True
		while flag and len(courses):
			flag = False
			removeList = []
			for x in courses:
				if degrees[x] == 0:
					for parent in parents[x]:
						degrees[parent] -= 1
					removeList.append(x)
					flag = True
			for x in removeList:
				courses.remove(x)
		return len(courses) == 0