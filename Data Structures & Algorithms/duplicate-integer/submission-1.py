class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDuplicate = set() # set maps out {1}, {2} so (Keys only)

        for i in nums: # iterate through nums array
            if i in isDuplicate: # create rule 
                return True 
            isDuplicate.add(i) # add keys to hashmap with applied rules
        return False