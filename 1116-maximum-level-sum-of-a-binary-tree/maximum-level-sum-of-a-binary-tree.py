# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return -1
        res = []
        q = [root]
        level = 1
        max_sum = float('-inf')
        max_level = 0
        while q:
            total = 0
            nxt_level = []
            for node in q:
                total += node.val
                if node.left:
                    nxt_level.append(node.left)
                if node.right:
                    nxt_level.append(node.right)
            q = nxt_level
            if total > max_sum :
                max_sum = total 
                max_level = level
            level += 1
        return max_level
                