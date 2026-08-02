# DNF
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval[0], newInterval[1]

        for i in range(len(intervals)):
            for j in range(i, len(intervals)):
                curr = intervals[i][j]
                if curr > newStart:
                    
