class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        n = len(s)
        reverse = ""
        for i in range(n-1, -1, -1):
            reverse += s[i]

        if s == reverse:
            return True
        else:
            return False