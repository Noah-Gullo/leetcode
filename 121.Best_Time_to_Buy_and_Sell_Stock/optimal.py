# Credit to [Matt Guest](https://www.youtube.com/watch?v=TeMz69mqHVA)
# Time O(N)
# Space O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointer problem
        max_profit = 0
        left = 0
        right = 1

        # While we can find available profits
        while right < len(prices):
            # If it is profitable meaning right price > left price.
            if prices[right] > prices[left]:
                # Calculate the current profit and compare against max_profit
                curr_profit = prices[right] - prices[left]
                max_profit = max(max_profit, curr_profit)
            # If it is not profitable move left to right
            else:
                left = right
            # Regardless of profitability, move right pointer along
            right += 1
                
        # Return calculated max profit.
        return max_profit;
