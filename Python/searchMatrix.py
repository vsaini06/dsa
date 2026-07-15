class Solution():
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        while left <= right:
            mid = left + (right - left) // 2
            row = mid // cols
            col = mid % cols
            value = matrix[row][col]
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

sol = Solution()
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(sol.searchMatrix(matrix1, 3))
print(sol.searchMatrix(matrix1, 13))
print(sol.searchMatrix([[1]], 1))
print(sol.searchMatrix([[1]], 2))