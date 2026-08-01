class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_map = {}
        sub_map[0] = 1
        total = count = 0
        for n in nums:
            total +=n
            if total - k in sub_map:
                count += sub_map[total-k]
            if total in sub_map:
                sub_map[total] += 1
            else:
                sub_map[total] = 1
        return count    