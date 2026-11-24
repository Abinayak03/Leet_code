# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        self.arr = []
        self.inorder(root)
        return self.arr
    def inorder(self, root):
        if root == None:
            return 
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
        