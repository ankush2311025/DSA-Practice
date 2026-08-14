class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = {}
        left = ans = 0
        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]] = 0
            freq[s[right]] += 1

            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1
            ans = max(ans,right-left+1)
        return ans