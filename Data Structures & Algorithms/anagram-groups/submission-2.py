class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        # Create hashmap to store the keys
        group = {}

        for word in strs:
            # Create key; tuple to split the sorted strs 
            key = tuple(sorted(word))
            group[key] = group.get(key, []) + [word]
        return list(group.values())
