class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_map = {}
        for i in s :
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        ans = 0
        odd = False
        for ch in hash_map:
            freq = hash_map[ch]
            ans += (freq//2)*2
            if freq % 2 == 1:
                odd = True
        if odd:
            ans += 1
        return ans



            