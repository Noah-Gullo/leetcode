class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        left = 0

        for right in range(len(chars) + 1):
            if right == len(chars) or chars[right] == " ":
                end = right - 1

                while left < end:
                    chars[left], chars[end] = chars[end], chars[left]
                    left += 1
                    end -= 1

                left = right + 1

        return "".join(chars)