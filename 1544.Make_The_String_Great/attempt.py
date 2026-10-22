# Time O(n)
# Space O(n)
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1] != char and stack[-1].lower() == char.lower():
                stack.pop()
            else:
                stack.append(s[curr])
                
        return "".join(stack)