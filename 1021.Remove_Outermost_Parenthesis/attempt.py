class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        res = ""
        for c in s:
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
            
            if c == "(" and count != 1:
                res += c
            elif c == ")" and count != 0:
                res += c

        return res