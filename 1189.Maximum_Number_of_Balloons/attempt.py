class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = {}
        for i in range(len(text)):
            if text[i] in counts:
                counts[text[i]] += 1
            else:
                counts[text[i]] = 1
        
        max_balloon = min(
            counts.get("b", 0),
            counts.get("a", 0),
            counts.get("l", 0) // 2,
            counts.get("o", 0) // 2,
            counts.get("n", 0)
        )
        
        return max_balloon

