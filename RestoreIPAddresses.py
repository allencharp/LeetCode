# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# 
# For example:
# Given "25525511135",
# 
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
class Solution:
	# @param s, a string
	# @return a list of strings
	def restoreIpAddresses(self, s):
		if(len(s) > 12 or len(s) < 4):
			return []
		rtnList = []
		# for the length of string is low 
		# so we can for many times!!!
		for p1 in range(len(s))[1::]:
			if(len(range(len(s))[p1::]) < 3):
				break
			for p2 in range(len(s))[p1::]:
				if(len(range(len(s))[p2::]) < 2):
					break;
				for p3 in range(len(s))[p2::]:
					if(len(range(len(s))[p3::]) < 1):
						break;
					ip1 = s[0:p1]
					ip2 = s[p1:p2]
					ip3 = s[p2:p3]
					ip4 = s[p3:len(s)]
					if(self.CheckIP(ip1) and self.CheckIP(ip2) and self.CheckIP(ip3) and self.CheckIP(ip4)):
						rtnList.append(ip1+'.'+ip2+'.'+ip3+'.'+ip4)
		return rtnList
					
	def CheckIP(self, ipN):
		try:
			# such as 010
			if(not(len(ipN) > 1 and ipN[0] == '0')):				
				num = int(ipN)
				if(num >= 0 and num <= 255):
					return True
		except:
			return False
		return False
			
		
s = Solution()
print s.restoreIpAddresses("010010")