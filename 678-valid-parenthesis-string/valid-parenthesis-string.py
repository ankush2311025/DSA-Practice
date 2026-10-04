class Solution:
    def checkValidString(self, s: str) -> bool:
        b_stack = []
        s_stack = []

        for i in range(len(s)):
            if s[i] == '(':
                b_stack.append(i)
            elif s[i] == '*':
                s_stack.append(i)
            else:
                if b_stack:
                    b_stack.pop()
                elif s_stack:
                    s_stack.pop()
                else:
                    return False
        while b_stack and s_stack :
            if b_stack[-1] > s_stack[-1]:
                return False
            b_stack.pop()
            s_stack.pop()
        return len(b_stack) == 0
            
            