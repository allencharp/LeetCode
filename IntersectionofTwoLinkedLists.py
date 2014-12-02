# Write a program to find the node at which the intersection of two singly linked lists begins.


# For example, the following two linked lists:

# A:          a1 → a2
                   # ↘
                     # c1 → c2 → c3
                   # ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.


# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# Credits:
# Special thanks to @stellari for adding this problem and creating all test cases.

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param two ListNodes
	# @return the intersected ListNode
	def getIntersectionNode(self, headA, headB):
		lengA = self.getLength(headA)
		lengB = self.getLength(headB)
		
		if lengA==0 or lengB==0:
			return None
		
		newHead = None
		if lengA > lengB:
			newHead = self.getNewList(headA, lengA-lengB)
			
			for i in range(lengB):
				if(headB.val == newHead.val):
					return headB
				else:
					headB = headB.next
					newHead = newHead.next
		
		else:
			newHead = self.getNewList(headB, lengB-lengA)
			
			for i in range(lengA):
				if(headA.val == newHead.val):
					return headA
				else:
					headA = headA.next
					newHead = newHead.next
		
	def getNewList(self, LongHead, diff):
		newHead = LongHead
		for i in range(diff):
			newHead = newHead.next
		
		return newHead
		
	
	def getLength(self, head):
		length = 0
		while(head != None):
			head = head.next
			length = length + 1
		
		return length
	

