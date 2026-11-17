# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        curr = head
        while curr and curr.next:
            if curr.val != curr.next.val:
                curr = curr.next
            else:
                prev = curr
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
        return head