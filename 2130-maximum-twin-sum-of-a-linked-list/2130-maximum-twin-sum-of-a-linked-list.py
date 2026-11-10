# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            Next = slow.next
            slow.next = prev
            prev = slow
            slow = Next
        head2 = prev
        max_sum = 0
        while head2:
            max_sum = max(max_sum, head.val+head2.val)
            head = head.next
            head2 = head2.next
            
        return max_sum