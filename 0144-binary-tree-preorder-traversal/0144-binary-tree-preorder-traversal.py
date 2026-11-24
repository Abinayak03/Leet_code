# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        self.arr = []
        self.preorder(root)
        return self.arr
    def preorder(self, root):
        if root == None:
            return 
        self.arr.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)