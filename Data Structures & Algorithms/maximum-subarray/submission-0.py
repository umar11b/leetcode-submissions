class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Video Attempt #1

        maxSubArray = nums[0] # first value in array
        currentSum = 0 # constantly computing current sum

        for n in nums:
            if currentSum  < 0: # if current sum is negative
                currentSum = 0 # reset back to 0
            currentSum += n # otherwise compute the maximum sum
            maxSubArray = max(maxSubArray, currentSum) # update the max sub array and max current sum
        return maxSubArray