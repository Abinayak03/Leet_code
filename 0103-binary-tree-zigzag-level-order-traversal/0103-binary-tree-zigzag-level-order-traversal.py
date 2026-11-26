# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root == None:
            return []
        ans = []
        queue = deque()
        queue.append(root)
        flag = True
        while queue:
            size = len(queue)
            level = deque()
            for i in range(size):
                node = queue.popleft()
                if flag:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(list(level))
            flag = not flag
        return ans