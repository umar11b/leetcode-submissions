class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Attempt 2
        # Create an empty hashmap to store groups
        groups = {}
        # Loop through each word in strs
        for word in strs:
            # Sort the word and convert to tuple to use as key
            key = tuple(sorted(word))
            # If key doesn't exist in hashmap, start a new list. If it does, append the word
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]


        # Return all the groups
        return list(groups.values())

