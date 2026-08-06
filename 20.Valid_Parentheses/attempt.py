# Time O(n)
# Explanation: Loops through all char in s
# Space O(n)
# Explanation: Creation of stack is n in worst case

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            curr = s[i]
            if curr == '(' or curr == "{" or curr == "[":
                stack.append(curr)
            elif curr == ')' or curr == "}" or curr == "]":
                if not stack:
                    return False
                match = stack[-1]
                if curr == ')' and match != '(' or curr == '}' and match != '{' or curr == ']' and match != '[':
                    return False
                else:
                    stack.pop()
            else:
                return False
        
        return not stack