# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while l1 != null and l2 != null:
            if l1 != null:
                l1 = l1.next
            if l2 != null:
                l2 = l2.next
        