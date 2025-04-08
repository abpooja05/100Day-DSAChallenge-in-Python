class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            triangle = self.generate(numRows - 1)
            last_row = triangle[-1]
            new_row = [1]  # First element is always 1
            for i in range(len(last_row) - 1):
                new_row.append(last_row[i] + last_row[i + 1])
            new_row.append(1)  # Last element is always 1
            triangle.append(new_row)
            return triangle