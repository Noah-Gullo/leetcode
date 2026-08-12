class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        res = []

        for c in s:
            if c == "(":
                if count > 0:
                    res.append(c)
                count += 1
            else:
                count -= 1
                if count > 0:
                    res.append(c)

        return "".join(res)