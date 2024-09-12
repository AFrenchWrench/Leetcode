"""
my solution for https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > 0:
                max_profit += price - min_price
                min_price = price

        return max_profit
