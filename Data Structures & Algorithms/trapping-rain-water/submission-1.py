class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]
        total = 0
    
        while l < r:
            if left_max < right_max:
                total += max(0,left_max - height[l])
                l += 1
            elif right_max < left_max:
                total += right_max - height[r]
                r -= 1
            else:
                total += max(0,left_max - height[l])
                l += 1
            left_max = max(left_max,height[l])
            right_max = max(right_max,height[r])
                
        return total