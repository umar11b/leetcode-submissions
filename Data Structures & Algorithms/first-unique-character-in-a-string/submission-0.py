class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Attempt 1
        # create hashmap
        count = {}

        # loop through characters in string
        # c gives you 'l', 'e', 'e', 't' 
        for c in s:
            # obtain count of repeated chars in string list
            # map them into the hashmap
            count[c] = count.get(c, 0) + 1

        # enumerate tuples (index:char, ...)
        for i, c in enumerate(s):
            # check if the count is equal to 1
            # return the index
            if count[c] == 1:
                return i
        return -1
    