# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        if not root :
            return []
        q = [root]
        ans = []
        front = 0
        while front < len(q):
            level_size = len(q) - front
            level = []
            for _ in range(level_size):
                node = q[front]
                front += 1
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans

