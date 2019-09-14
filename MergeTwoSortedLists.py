# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None and l2 is None:
            return None

        r1 = r2 = ListNode(0)


        while l1 or l2:
            if l1 is None:
                r2.val = l2.val
                r2.next = l2.next
                break
            elif l2 is None:
                r2.val = l1.val
                r2.next = l1.next
                break
            else:
                if l1.val >= l2.val:
                    r2.val = l2.val
                    r2.next = ListNode(0)
                    r2 = r2.next
                    l2 = l2.next
                else:
                    r2.val = l1.val
                    r2.next = ListNode(0)
                    r2 = r2.next
                    l1 = l1.next
        return r1


# l1
num1 = ListNode(1)
num3 = ListNode(3)
num4 = ListNode(4)
num1.next = num3
num3.next = num4
# num1 = ListNode(1)
# num1.next = None

# l2
val1 = ListNode(1)
val2 = ListNode(2)
val3 = ListNode(3)
val4 = ListNode(4)
val5 = ListNode(5)
val1.next = val2
val2.next = val3
val3.next = val4
val4.next = val5

s = Solution()
result = s.mergeTwoLists(num1, val1)

while result:
    print(result.val)
    result = result.next
