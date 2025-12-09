from pathlib import Path

def calculate_day_4_answers():
    def count_adjacent_rolls(grid, row, col):
        rows, cols = len(grid), len(grid[0])
        return sum(grid[i][j] == '@' for i in range(row-1, row+2) for j in range(col-1, col+2) if 0 <= i < rows and 0 <= j < cols) - 1

    def solve_part_1(grid):
        rows, cols = len(grid), len(grid[0])
        accessible_rolls = sum(grid[i][j] == '@' and count_adjacent_rolls(grid, i, j) < 4 for i in range(rows) for j in range(cols))
        print("Part 1:", accessible_rolls)

    def solve_part_2(grid):
        rows, cols = len(grid), len(grid[0])
        total_removed = 0
        while True:
            removed_rolls = 0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == '@' and count_adjacent_rolls(grid, i, j) < 4:
                        grid[i][j] = '.'
                        removed_rolls += 1
            if removed_rolls == 0:
                break
            total_removed += removed_rolls
        print("Part 2:", total_removed)

    data_path = Path(__file__,"..", "..", "data", "day4.txt").resolve()
    with open(data_path, 'r') as file:
        grid = [list(line.strip()) for line in file]

    solve_part_1(grid)
    solve_part_2([row[:] for row in grid])

if __name__ == "__main__":
    calculate_day_4_answers()