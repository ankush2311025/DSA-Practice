class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        c = 0
        for x in nums :
            c += m - x
        return c