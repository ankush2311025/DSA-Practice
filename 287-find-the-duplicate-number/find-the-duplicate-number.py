class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1
        for i in range(len(nums)):
            if hash_map[nums[i]] > 1 :
                return nums[i]
            