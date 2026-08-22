class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        f = 0 
        d = {}
        r = [int(i) for i in str(n)]
        for i in r: 
            d[i] = d.get(i, 0) + 1
        for i in d: 
            f += d[i] * i 
        return f 
        