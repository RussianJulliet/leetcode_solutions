# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        head = first = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                first.next = l1
                l1 = l1.next
            else:
                first.next = l2
                l2 = l2.next
            first = first.next
        first.next = l1 or l2
        return head.next
