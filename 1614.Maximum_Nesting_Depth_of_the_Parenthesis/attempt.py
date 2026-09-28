# Time O(n)
# Space O(n)
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxDepth = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
                if len(stack) > maxDepth:
                    maxDepth = len(stack)
            elif s[i] == ")":
                stack.pop(0)

        return maxDepth