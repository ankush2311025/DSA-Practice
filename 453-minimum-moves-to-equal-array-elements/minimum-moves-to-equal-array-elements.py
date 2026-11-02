class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m = min(nums)
        count = 0 
        for i in nums:
            count += abs(m-i)
        return count 