class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for day , temp in enumerate(temperatures):
            if not stack:
                stack.append((day,temp))
                continue
            if stack[-1][1] >= temp:
                stack.append((day,temp))
                
            while stack and stack[-1][1] < temp:
                result[stack[-1][0]] += abs(stack[-1][0] - day)
                stack.pop()
                if not stack:
                    stack.append((day,temp))
                else:
                    if stack[-1][1] >= temp:
                        stack.append((day,temp))
        return result