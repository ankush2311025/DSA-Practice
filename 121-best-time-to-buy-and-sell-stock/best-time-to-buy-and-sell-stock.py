class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i = 0 
        j = 1
        mx_pr = 0 
        while j <= len(prices)-1:
            profit = prices[j] - prices[i]
            if profit > mx_pr:
                mx_pr = profit
            if prices[i] > prices[j]:
                i = j 
            j += 1
        return mx_pr