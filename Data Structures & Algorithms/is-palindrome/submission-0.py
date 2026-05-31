class Solution:
    def isPalindrome(self, s: str) -> bool:
        
    # string s exists
    # if palindrome, return true
    # else false
        l, r  = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            # compare strings
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True

        # palindrome = string reads same forward/backward
        # case sensitive, ignores all non-alphanomarical chars

