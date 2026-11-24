# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def isMirror(p, q):   
            if p == None and q == None: 
                return True
            if p == None or q == None: 
                return False
            if p.val != q.val:
                return False
            left_ = isMirror(p.left, q.right)
            right_ = isMirror(p.right, q.left)
            return left_ and right_
        if root == None:
            return True
        return isMirror(root.left, root.right)
    