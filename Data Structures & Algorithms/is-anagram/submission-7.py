class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Validate if the length of both strings even match
        if len(s) != len(t):
            return False
        
        # Create a hashmap to populate 
        countT, countS = {}, {}

        # I would iterate through the range of s, then add to hashmap
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1


        # compare hashmap with t array, if not equal return false
        if countS != countT:
            return False
        
        # else return true
        return True



