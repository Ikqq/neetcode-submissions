class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []
        total = 0
        
        max_prefix = 0
        for i in range(len(height)):
            max_prefix = max(max_prefix,height[i])
            prefix.append(max_prefix)
        
        max_suffix = 0
        for i in range(len(height)-1,-1,-1):
            max_suffix = max(max_suffix,height[i])
            suffix.append(max_suffix)
            
        suffix = suffix[::-1]
        
        for j in range(len(height)):
            total += max(0,(min(prefix[j],suffix[j]) - height[j]))
        
        return total
        


