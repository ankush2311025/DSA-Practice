class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0 
        r = len(height)-1
        max_arr = 0
        while l < r :
            if height[l] < height[r] :
                area = height[l] * (r-l)
                l += 1
            else :
                area = height[r] * (r-l)
                r -= 1
            max_arr = max(area , max_arr)
        return max_arr