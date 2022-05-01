'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = prices[0]
        max_profit = 0 
        for i in range(1,len(prices)): 
            if current_min > prices[i]: 
                current_min = prices[i]
                continue 
            if prices[i] - current_min > max_profit: 
                max_profit = prices[i] - current_min
        return max_profit
