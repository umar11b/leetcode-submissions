class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        myhash = {}
        for n in nums:
            if n in myhash:
                return True
            myhash[n] = True
        return False