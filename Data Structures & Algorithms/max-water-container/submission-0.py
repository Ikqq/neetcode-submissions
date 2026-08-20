class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_ = 0
        while i < j:
            if (j - i) * min(heights[i], heights[j]) > max_:
                max_ = (j - i) * min(heights[i], heights[j])
            if min(heights[i], heights[j]) == heights[i]:
                i += 1
            else:
                j -= 1
        return max_
    
            

