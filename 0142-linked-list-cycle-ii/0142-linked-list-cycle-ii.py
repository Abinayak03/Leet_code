# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow_2 = head
                while True:
                    if slow == slow_2:
                        return slow #check first, [1,0]
                    slow = slow.next
                    slow_2 = slow_2.next
                    
        return None