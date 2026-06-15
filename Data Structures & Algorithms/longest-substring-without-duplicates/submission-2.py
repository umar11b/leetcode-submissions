class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # attempt 1
        # create 2 pointer and hashmap to store counts
        l = 0
        tracker = 0
        count = set()

        for r, c in enumerate(s):
            # if c is in the hashset, then 
            while l < r and c in count:
                count.remove(s[l])
                l += 1
            count.add(c)
            tracker = max(tracker, r - l +1)
        return tracker