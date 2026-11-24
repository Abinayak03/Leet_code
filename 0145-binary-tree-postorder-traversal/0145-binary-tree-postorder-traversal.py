# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # donot add arr=[] here as if a previous execution appended [3, 2, 1], those values would remain.
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        self.arr = []
        self.postorder(root)
        return self.arr
    def postorder(self, root):
        if root == None:
            return 
        self.postorder(root.left)
        self.postorder(root.right)
        self.arr.append(root.val)