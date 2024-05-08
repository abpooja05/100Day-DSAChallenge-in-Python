class Solution:
    def addDigits(self, num: int) -> int:
        total = 0
        for digit in str(num):
          total += int(digit)
          if total >= 10:
            total = self.addDigits(total)
        return total
