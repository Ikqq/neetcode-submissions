class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = "".join(char for char in s if char.isalnum())
        x = s_.lower()
        length = len(x) // 2
        if len(x) % 2 == 0:
            half_1 = x[:length]
            half_2 = x[length:][::-1]
        else:
            half_1 = x[:length]
            half_2 = x[length+1:][::-1]

        return half_2 == half_1