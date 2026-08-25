# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def dfs(tree, k):
            if not tree:
                return
    
            if tree.val < k:
                if not tree.right:
                    tree.right = TreeNode(k)
                    return
                dfs(tree.right, k)
            else:
                if not tree.left:
                    tree.left = TreeNode(k)
                    return 
                dfs(tree.left, k)
        dfs(root, val)
        return root