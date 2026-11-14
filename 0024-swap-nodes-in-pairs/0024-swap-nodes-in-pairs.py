# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr and curr.next:
            Next = curr.next
            curr.next = Next.next
            Next.next = prev.next
            prev.next = Next
            prev = curr
            curr = prev.next
        return dummy.next