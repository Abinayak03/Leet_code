# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next
        
        curr = prev.next
        prev_node = None

        for _ in range(right - left+1):
            Next = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = Next
        left_end = prev.next
        prev.next = prev_node
        left_end.next = curr
        return dummy.next