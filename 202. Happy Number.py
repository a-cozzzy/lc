class Solution:
    def sq(self, n: int) -> int:
        res = 0
        while n > 0:
            digit = n % 10
            res += digit * digit
            n = n // 10
        return res

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sq(n)
        return n == 1
