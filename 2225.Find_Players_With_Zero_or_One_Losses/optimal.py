class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero = set()
        one = set()
        many = set()

        for winner, loser in matches:
            if winner not in one and winner not in many:
                zero.add(winner)
            if loser in zero:
                zero.discard(loser)
                one.add(loser)
            elif loser in one:
                one.discard(loser)
                many.add(loser)
            elif loser in many:
                continue
            else:
                one.add(loser)
        
        return [sorted(list(zero)), sorted(list(one))]