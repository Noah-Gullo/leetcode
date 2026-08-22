class Solution:
    def countPoints(self, rings: str) -> int:
        hash_table = {}

        for curr in range(0, len(rings), 2):
            letter = rings[curr]
            position = rings[curr + 1]

            if position not in hash_table:
                hash_table[position] = set()

            hash_table[position].add(letter)

        count = 0
        for position in hash_table:
            if len(hash_table[position]) == 3:
                count += 1

        return count