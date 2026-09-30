# Time O(nlogn)
# Space O(n)
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        counts = {}
        answer = [[],[]]

        for i in range(len(matches)):
            if matches[i][1] in counts:
                counts[matches[i][1]] += 1
            else:
                counts[matches[i][1]] = 1

        for i in range(len(matches)):
            if matches[i][0] not in counts:
                counts[matches[i][0]] = 0
        
        for key, value in counts.items():
            if value == 0:
                answer[0].append(key)
            elif value == 1:
                answer[1].append(key)
        
        answer[0].sort()
        answer[1].sort()
        return answer