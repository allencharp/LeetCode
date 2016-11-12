# Reverse a singly linked list.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
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
            
            
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
a = ListNode(1)
b = ListNode(2)
#c = ListNode(3)
a.next = b
#b.next = c

s = Solution()
s.reverseList(a)

start = b
while(start):
    print start.val
    start = start.next