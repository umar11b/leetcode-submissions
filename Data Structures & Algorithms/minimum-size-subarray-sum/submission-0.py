class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # init the vars
        l = 0
        currSum = 0
        minLen = float('inf')

        for r in range(len(nums)):
            currSum = currSum + nums[r]

            while currSum >= target:
                minLen = min(minLen, r - l + 1)
                currSum = currSum - nums[l]
                l += 1
        return minLen if minLen != float('inf') else 0


