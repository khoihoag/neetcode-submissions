# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        root = TreeNode(-999999999, root)
        def dfs(root):
            if not root:
                return
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if root.left is None and root.right is None and root.val == target:
                return None
            return root
        dfs(root)
        if root.left:
            return root.left
        return None