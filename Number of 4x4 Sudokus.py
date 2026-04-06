def count_4x4_sudoku_solutions():
    """Count all valid complete 4x4 Sudoku grids using backtracking."""
    grid = [0] * 16  # 4x4 grid as flat array

    def is_valid(pos, val):
        row, col = divmod(pos, 4)
        # Check row
        for c in range(4):
            if grid[row * 4 + c] == val:
                return False
        # Check column
        for r in range(4):
            if grid[r * 4 + col] == val:
                return False
        # Check 2x2 box
        br, bc = (row // 2) * 2, (col // 2) * 2
        for r in range(br, br + 2):
            for c in range(bc, bc + 2):
                if grid[r * 4 + c] == val:
                    return False
        return True

    def solve(pos):
        if pos == 16:
            return 1
        count = 0
        for val in range(1, 5):
            if is_valid(pos, val):
                grid[pos] = val
                count += solve(pos + 1)
                grid[pos] = 0
        return count

    return solve(0)


if __name__ == "__main__":
    result = count_4x4_sudoku_solutions()
    print(f"Total valid 4x4 Sudoku solutions: {result}")
