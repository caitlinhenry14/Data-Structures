class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            if i >= 2:
                for j in range(1, i):
                    row[j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
            pascal_triangle.append(row)
        return pascal_triangle
