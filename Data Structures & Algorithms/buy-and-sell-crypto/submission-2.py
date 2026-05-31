class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointer solution
        # left pointer = buy
        # right pointer = sell
        # Time: O(n), Space: O(1) since we only used pointers

        l, r = 0,1 # left=buy, right=sell
        maxProfit = 0 # starting value as 0

        # while r iterates through the length of prices array
        while r < len(prices):
            # is this profitable? if buy price is less than sell price
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l] # sell - buy = profit
                maxProfit = max(maxProfit, profit)
            else: # if not profitable then
                l = r # shift left pointer all the way to the right pointer
            r += 1 # shift right by 1
        return maxProfit


            

