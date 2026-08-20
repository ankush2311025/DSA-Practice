# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = [root]
        res = []
        front = 0
        while front < len(q):
            level_sum = 0
            level_size = len(q) - front 

            for _ in range(level_size):
                node = q[front]
                front += 1
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_sum)
        res.sort()

        if k > len(res):
            return -1
        return res[-k]