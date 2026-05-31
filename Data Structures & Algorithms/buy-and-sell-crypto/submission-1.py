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

            


        
        
        
        
        
        
        
        
        
        
        
        # int array prices
        # prices[i] where i = day of the price
        # buy one day, sell another day
        # return maximum profit we can achieve
        # if no transactions return 0
        
        # holds profit values
        # hashSet = set()

        # for i in prices:
        #     profit = hashSet - profit[i]
        #     # if the
        #     if hashSet[prices] != profit:
        #         return 0
        # return [] #First attempt - 15 mins


            

