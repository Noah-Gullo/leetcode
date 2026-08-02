# Time O(n^2) 
# Explanation: This solution loops through n prices then for each price loops through every following price
# Space O(1)
# Explanation: The only allocation are variables to keep track. No other data structures are allocated.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Keep track of max profit
        max_profit = 0

        # Loop through all prices
        for i in range(len(prices)):
            # Current price
            curr = prices[i]
            # Loop through every price following current price
            for j in range(i, len(prices)):
                # Calculate the current profit as the current following price - current price
                compare = prices[j]
                profit = compare - curr
                # If the current profit is greater than the saved max profit replace it
                if profit > max_profit:
                    max_profit = profit
        
        # Returns 0 if no profit is found, otherwise it correctly return the maximum found profit
        return max_profit;
