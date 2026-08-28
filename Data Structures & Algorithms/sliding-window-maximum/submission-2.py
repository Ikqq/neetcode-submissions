from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() #collect only index current value, index max value, index value that less than the index new value
        for r in range(len(nums)): 
            new_nums = nums[r]
            while q and nums[q[-1]]< new_nums: # remove the current index if the    next number has more than the current
                q.pop()
            q.append(r)
            if q[0] < r - k + 1: # remove char which not in window
                q.popleft()
            if r >= k - 1:  #add the max value to res
                res.append(nums[q[0]])
        return res