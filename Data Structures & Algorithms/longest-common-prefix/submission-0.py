class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # attempt 1 
        # starting value for prefix declared
        prefix = strs[0]

        # loop through the list of strings
        for c in range(len(prefix)):
            for word in strs:
                if c >= len(word):
                    return prefix[:c]
                if prefix[c] != word[c]:
                    return prefix[:c]
        return prefix

