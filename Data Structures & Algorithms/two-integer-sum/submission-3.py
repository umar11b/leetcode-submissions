class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create the hashmap
        # When iterating through the your array, you cant reuse an indexed value
        # we need to use the difference (target 4 - value 1 = 3) to find
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            # if index:value exists in the hashmap, then rest
            if diff in prevMap:
                return [prevMap[diff], i]
            # if we cant find index, we need to update hashmap
            prevMap[n] = i
        return
            

        
