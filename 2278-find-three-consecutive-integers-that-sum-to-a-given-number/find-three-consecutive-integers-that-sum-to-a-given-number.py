class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        if num == 0:
            return [-1,0,1]
        if num % 3 != 0 :
            return []
        return [num//3-1,num//3,num//3+1]