# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next:
            return 
        curr = head
        slow = curr
        fast = curr.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second!=None:
            Next = second.next
            second.next = prev
            prev = second
            second = Next

        head2 = prev
        curr = head
        while head2:
            next1 = curr.next
            next2 = head2.next

            curr.next = head2
            head2.next = next1
            curr = next1
            head2 = next2