class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)-2):
            if len(set([s[i],s[i+1],s[i+2]])) == 3:
                count += 1
            else :
                count += 0
        return count 
