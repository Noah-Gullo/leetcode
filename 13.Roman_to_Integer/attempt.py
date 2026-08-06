class Solution:
    def romanToInt(self, s: str) -> int:
        curr = 0
        nxt = 1
        res = 0
        while curr < len(s):
            special = False
            if s[curr] == "I":
                if nxt < len(s) and s[nxt] == "V":
                    res += 4
                    special = True
                elif nxt < len(s) and s[nxt] == "X":
                    res += 9
                    special = True
                else:
                    res += 1
            elif s[curr] == "V":
                res += 5
            elif s[curr] == "X":
                if nxt < len(s) and s[nxt] == "L":
                    res += 40
                    special = True
                elif nxt < len(s) and s[nxt] == "C":
                    res += 90
                    special = True
                else:
                    res += 10
            elif s[curr] == "L":
                res += 50
            elif s[curr] == "C":
                if nxt < len(s) and s[nxt] == "D":
                    res += 400
                    special = True
                elif nxt < len(s) and s[nxt] == "M":
                    res += 900
                    special = True
                else:
                    res += 100
            elif s[curr] == "D":
                res += 500
            elif s[curr] == "M":
                res += 1000

            if not special:
                curr += 1
                nxt += 1
            else:
                curr += 2
                nxt += 2
        return res