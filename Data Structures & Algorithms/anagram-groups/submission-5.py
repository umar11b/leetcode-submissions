class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Attempt 3
        # create hashmap to store each grouped word
        groups = {}

        # loop through list of strs for word
        for word in strs:
            # create a key based on sorted words
            # list is immutable so python can make it a key 
            key = tuple(sorted(word))

            # after looping through our word list we need to add to list
            if key in groups:
                groups[key].append(word) # append the grouped words
            else:
                groups[key] = [word] # empty new section for any new groups
        return list(groups.values())

        

