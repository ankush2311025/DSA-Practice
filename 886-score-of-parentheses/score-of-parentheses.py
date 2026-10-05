class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i in s :
            if i == '(':
                stack.append(0)
            else:
                l = stack.pop()
                if l == 0 :
                    score = 1
                else:
                    score = 2 * l
                stack[-1] += score
        return  stack[0]
