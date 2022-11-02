# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], c=0) -> Optional[ListNode]:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            value = l1.val + l2.val + c
            c = value // 10
            answer = ListNode(value % 10)

            if (l1.next != None) or (l2.next != None) or (c != 0):
                if l1.next == None:
                    l1.next = ListNode(0)
                if l2.next == None:
                    l2.next = ListNode(0)
                answer.next = self.addTwoNumbers(l1.next, l2.next, c)
            return answer
