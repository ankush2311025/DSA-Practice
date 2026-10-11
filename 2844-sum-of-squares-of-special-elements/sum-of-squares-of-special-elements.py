class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        special = 0
        for i in range(1,len(nums)+1):
            if n % i == 0:
                special += nums[i-1]*nums[i-1]
        return special