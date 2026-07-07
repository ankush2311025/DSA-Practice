class Solution:
    def sumAndMultiply(self, n: int) -> int:
        ans = ''
        s = 0 
        while n > 0 :
            x = n % 10
            n = n//10
            s += x
            if x == 0:
                continue

            ans = str(x) + ans
        if ans == '':
            return 0
        return int(ans)*s
        
        