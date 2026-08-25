from collections import defaultdict
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        dupli = defaultdict(int)
        max_frequency = 0
        max_length = 0
        while right != len(s):
            dupli[s[right]] += 1
            max_frequency = max(max_frequency,dupli[s[right]])
            while right - left + 1 - max_frequency > k:
                dupli[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length