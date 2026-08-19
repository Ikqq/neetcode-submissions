class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = "".join(char for char in s if char.isalnum())
        x = s_.lower()

        return x[::-1] == x