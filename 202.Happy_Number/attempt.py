class Solution:
    def isHappy(self, n: int) -> bool:
        found = set()
        while n != 1 or n not in found:
            squares = []
            while n > 9:
                digit = n % 10
                squares.append(digit*digit)
                n //= 10
            squares.append(n * n)
            total = 0
            for i in range(len(squares)):
                total += squares[i]
            
            if total in found:
                return False
            elif total == 1:
                return True
            else:
                found.add(total)
                n = total
