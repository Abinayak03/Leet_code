# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next:
            return head
        n = 1
        point = head
        while point.next:
            point = point.next
            n += 1
        k = k%n
        if k == 0:
            return head
        slow = head
        fast = head
        for _ in range(k):
            slow = slow.next
        while slow and slow.next:
            slow = slow.next
            fast = fast.next
        head2 = fast.next
        fast.next = None
        slow.next = head
        return head2