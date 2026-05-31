class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a hashset (since we are only looking for n)
        # n is the value in array nums (1,2,3,5)
        # Hashset: Time: O(n), Space: O(n)

        hashSet = set()

        # loop through array
        for n in nums:
            # if n exists in the hashset return true
            if n in hashSet:
                return True
            # if not, just add the value to the set and move onto next value
            hashSet.add(n)
        return False

            