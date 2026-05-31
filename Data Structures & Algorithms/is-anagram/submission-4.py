class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # compare string lengths
        if len(s) != len(t):
            return False
        
        mapS, mapT = {}, {}

        if Counter(s) == Counter(t):
            return True
        
        for i in range(len(s)):
            # logic: count characters inside one hashmap
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)
        for c in mapS:
            if mapS[c] != mapT.get(c, 0):
                return False
        return True