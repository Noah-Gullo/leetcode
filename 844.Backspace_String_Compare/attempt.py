# Time O(n)
# Space O(n)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []

        for char in s:
            if char != "#":
                s_stack.append(char)
            else:
                if s_stack != []:
                    s_stack.pop()

        s_res = "".join(s_stack)

        t_stack = []
        for char in t:
            if char != "#":
                t_stack.append(char)
            else:
                if t_stack != []:
                    t_stack.pop()
        t_res = "".join(t_stack)
        return s_res == t_res
