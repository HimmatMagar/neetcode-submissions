class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "+":
                new_num = stack[-1] + stack[-2]
                stack.append(new_num)
            elif i == "D":
                stack.append(stack[-1] * 2)
            elif i == "C":
                stack.pop()
            else:
                num = int(i)
                stack.append(num)
        
        return sum(stack)