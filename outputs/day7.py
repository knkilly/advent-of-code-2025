from pathlib import Path

from functools import lru_cache


def calculate_day_7_answers():
    data_path = Path(__file__,"..", "..", "data", "day7.txt").resolve()
    def calculate_part_2_answer(grid):
        rows = len(grid)
        cols = len(grid[0])
        start_col = grid[0].index("S")
        @lru_cache(None)
        def dfs(r, c):
            # Out of bounds → no timeline
            if c < 0 or c >= cols:
                return 0
            # Past bottom → one completed timeline
            if r >= rows:
                return 1
            if grid[r][c] == "^":
                # Split left and right
                return dfs(r+1, c-1) + dfs(r+1, c+1)
            else:
                # Continue straight down
                return dfs(r+1, c)

        return dfs(1, start_col)

    def calculate_part_1_answer(grid):
        rows = len(grid)
        cols = len(grid[0])
        # Find start position
        start_col = grid[0].index("S")
        beams = {(1, start_col)}  # start just below S
        splits = 0

        while beams:
            new_beams = set()
            for r, c in beams:
                if r >= rows:
                    continue
                if grid[r][c] == "^":
                    splits += 1
                    if c > 0:
                        new_beams.add((r+1, c-1))
                    if c < cols-1:
                        new_beams.add((r+1, c+1))
                else:
                    new_beams.add((r+1, c))
            beams = new_beams
        return splits

    with open(data_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
        print("Part 1:", calculate_part_1_answer(grid))
        print("Part 2:", calculate_part_2_answer(grid))

if __name__ == "__main__":
    calculate_day_7_answers()
