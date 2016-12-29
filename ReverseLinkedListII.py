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
		
		begin_node = None
		finish_node = None
		
		count = 1
		while(head):
			if m == 0:
				isStartFromFirst = True
			elif count + 1 == m:
				begin_node = head
			
			if count == m:
				startNode = head
					
			if count == n:
				endNode = head
				if head.next is None:
					isEndFromLast = True
				else:
					finish_node = head.next
				
			count += 1
			head = head.next
			
		newStart = self.reverseList(startNode, endNode)
		begin_node.next = newStart
		if not isEndFromLast:
			while(newStart):
				if newStart.next is None:
					newStart.next = begin_node
				else:
					newStart = newStart.next
					
		
	
	def reverseList(self, head, end):
		if head is None or head.next is None:
			return head
		
		cur = head
		nxt = head.next
		
		headflag = True;
		while nxt:
			if nxt is end:
				return cur
			
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

a = ListNode(1)
b = ListNode(2)
a.next = b
c = ListNode(3)
b.next = c
d = ListNode(4)
c.next = d
s = Solution()
print s.reverseBetween(a,2,3)