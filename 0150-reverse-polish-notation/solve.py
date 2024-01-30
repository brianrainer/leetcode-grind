from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for c in tokens:
            if c not in "+-*/":
                s.append(int(c))
                continue
            y, x = s.pop(), s.pop()
            if c == '+':
                s.append(x+y)
            if c == '*':
                s.append(x*y)
            if c == '-':
                s.append(x-y)
            if c == '/':
                s.append(int(x/y))
        return s.pop()
