# Given a sorted linked list, delete all duplicates such that each element appear only once.
# 
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

#Definition for singly-linked list.


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def deleteDuplicates(self, head):
		
		if(head == None or head.next == None):
			return head
		
		potNode = ListNode(head.val)
		rtnNode = potNode 
		
		while(head and head.next):
			head = head.next
			
			nextValue = head.val
			potValue = potNode.val
			
			if(nextValue == potValue):
				continue		
			else:
				potNode.next = ListNode(head.val)
				potNode = potNode.next
		
		return rtnNode;
				


def main():
	n1 = ListNode(1)
	n2 = ListNode(2)
	n3 = ListNode(2)

	n1.next = n2
	n2.next = n3

	
	s = Solution()
	n = s.deleteDuplicates(n1)
	while(n):
		print n.val
		n = n.next
	
if __name__ == "__main__":
	main()
