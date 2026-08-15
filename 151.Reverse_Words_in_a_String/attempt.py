class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        i = len(s) - 1
        while i >= 0:
            word = ''
            while i >= 0 and s[i] != ' ':
                word = s[i] + word
                i -= 1
            if word:
                res += word + ' '
            while i >= 0 and s[i] == ' ':
                i -= 1