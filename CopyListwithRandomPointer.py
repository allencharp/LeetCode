class RandomListNode:
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution:
    
	
	# @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):

		if head == None:
			return None

		dict = {}
		copyHead = None
		
		temp = head

		previous = None
		# init the label and next, not random
		while(temp != None): # label = 1
			
			copyHead = RandomListNode(temp.label)
			
			copyHead.next = temp.next
			copyHead.random = temp.random
			if(previous != None):
				dict[previous].next = copyHead
			
			dict[temp] = copyHead
			
			previous = temp

			temp = temp.next
	
		
		temp = head

		while(temp != None):
			random = temp.random

			if(random == None):
				dict[temp].random = None
			else:
				dict[temp].random = dict[random]
			temp = temp.next
			
		temp = head
		return dict[temp]

		
r1 = RandomListNode(1)
r2 = RandomListNode(2)
r1.next = r2
r1.random = r2
r2.next = None
r2.random = r2

s = Solution()
print s.copyRandomList(r1).label
print s.copyRandomList(r1).random.label
print s.copyRandomList(r1).next.label
print s.copyRandomList(r1).next.random
