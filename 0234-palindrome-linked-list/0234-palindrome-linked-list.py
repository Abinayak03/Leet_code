# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
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
        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True