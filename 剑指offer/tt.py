class Solution:
    def moving_count(self, threshold, rows, cols):
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0
        visited = [False for i in range(rows * cols)]
        count = self.moving_count_core(threshold, rows, cols, 0, 0, visited)
        return count

    def moving_count_core(self, threshold, rows, cols, row, col, visited):
        count = 0
        if self.check(threshold, rows, cols, row, col, visited):
            visited[row * cols + col] = True
            count = 1 + self.moving_count_core(threshold, rows, cols, row - 1, col, visited) + self.moving_count_core(
                threshold, rows, cols, row + 1, col, visited) + self.moving_count_core(threshold, rows, cols, row,
                                                                                       col - 1,
                                                                                       visited) + self.moving_count_core(
                threshold, rows, cols, row, col + 1, visited)
        return count

    def check(self, threshold, rows, cols, row, col, visited):
        if 0 <= row < rows and 0 <= col < cols and self.get_digit_sum(row) + self.get_digit_sum(
                col) <= threshold and not visited[row * cols + col]:
            return True
        return False

    def get_digit_sum(self, number):
        sum = 0
        while number > 0:
            sum += number % 10
            number //= 10
        return sum


print(Solution().moving_count(5, 10, 10))