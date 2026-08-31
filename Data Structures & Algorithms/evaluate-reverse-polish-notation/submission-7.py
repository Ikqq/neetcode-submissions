class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for i in tokens:
            if i in "+-*/":
                x = num_stack.pop()
                y = num_stack.pop()
                if i == "+":
                    total = y + x
                elif i == "-":
                    total = y - x
                elif i == "*":
                    total = y * x
                elif i == "/":
                    total = int(y / x)
                num_stack.append(total)
            else:
                num_stack.append(int(i))
        return int(num_stack[0])