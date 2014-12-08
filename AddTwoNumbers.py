# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
	
		isAboveTen = False
		lastNode = None
		firstNode = None
		node = None
		while(l1 != None or l2 != None):
			
			add1 = l1.val if l1 != None else 0
			add2 = l2.val if l2 != None else 0
			
			result = add1 + add2
			
			result = result + 1 if isAboveTen else result
			
			if(result >= 10):
				isAboveTen = True
			else:
				isAboveTen = False
			
			result = (result) - 10 if result >= 10 else result
					
			node = ListNode(result)	
					
			if(lastNode != None):
				lastNode.next = node
			else:
				firstNode = node
			
			lastNode = node
			
			if(l1 != None):
				l1 = l1.next
			if(l2 != None):
				l2 = l2.next
		
		if(isAboveTen):
			node = ListNode(1)
			lastNode.next = node
			
		return firstNode
		
O11 = ListNode(2)
O12 = ListNode(4)
O13 = ListNode(3)
O11.next = O12
O12.next = O13


L11 = ListNode(5)
L12 = ListNode(6)
L13 = ListNode(4)
L11.next = L12
L12.next = L13


s = Solution()
print s.addTwoNumbers(O11, L11).val