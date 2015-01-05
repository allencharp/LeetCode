class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
	def compareVersion(self, version1, version2):
		if(version1 is None):
			return -1
		if(version2 is None):
			return 1
		
		array1 = self.GetVersionArray(version1)
		array2 = self.GetVersionArray(version2)
			
		m = max(len(array1), len(array2))
		for i in range(m):
			value1 = 0 if i+1 > len(array1) else int(array1[i])
			value2 = 0 if i+1 > len(array2) else int(array2[i])
			
			if(value1 > value2):
				return 1
			elif(value1 < value2):
				return -1
			else:
				continue
		return 0

	def GetVersionArray(self, version):
		array = version.split('.')

		return array

s = Solution()
print s.compareVersion("01", "1")