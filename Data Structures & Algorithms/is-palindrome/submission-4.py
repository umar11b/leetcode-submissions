class Solution:
    def isPalindrome(self, s: str) -> bool:
        # attempt 1
        # Initialize left and right pointers
        l, r = 0, len(s) - 1

        # Loop while left is less than right
        while l < r:
            while l < r and not s[l].isalnum():
                    l += 1
            while l < r and not s[r].isalnum():
                    r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True

            

