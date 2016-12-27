# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
# return 1->4->3->2->5->NULL.
#
# Note:
# Given m, n satisfy the following condition:
# 1 <= m <= n <= length of list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	
	def reverseBetween(self, head, m, n):
		
		if(head is None or head.next is None):
			return head
		
		isStartFromFirst = False;
		isEndFromLast = False;
		
		startNode = None
		endNode = None
		
		count = 1
		while(head):
			if m == 0:
				isStartFromFirst = True
			if count == m:
				startNode = head
			if count == n:
				endNode = head
			
			count += 1
			head = head.next
			
		
	
	def reverseList(self, head):
		if head is None or head.next is None:
			return head
		
		cur = head
		nxt = head.next
		
		headflag = True;
		while nxt:
			temp = ListNode(cur.val)
			temp.next = nxt
			
			if nxt.next:
				temp.next = nxt.next
			else:
				temp.next = None
			
			if headflag:
				cur.next = None
				headflag = False
			
			nxt.next = cur
			cur = nxt
			nxt = temp.next
		
		return cur
print range(4)