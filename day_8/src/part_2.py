def calculate_score(row, col, grid, score_grid):
    target_tree_height = grid[row][col]
    n_rows = len(grid)
    n_cols = len(grid[0])

    directions = [
        # North
        {
            "row_slice": [0, row],
            "col_slice": [col, col+1],
            "is_toward_southeast": False
        },
        # East
        {
            "row_slice": [row, row+1],
            "col_slice": [col+1, n_cols],
            "is_toward_southeast": True
        },
        # South
        {
            "row_slice": [row+1, n_rows],
            "col_slice": [col, col+1],
            "is_toward_southeast": True
        },
        # West
        {
            "row_slice": [row, row+1],
            "col_slice": [0, col],
            "is_toward_southeast": False
        }
    ]

    score = 1
    for direction in directions:
        directional_score = calculate_scenic_score_for_direction(
            grid,
            direction["row_slice"],
            direction["col_slice"],
            target_tree_height,
            direction["is_toward_southeast"]
        )
        score *= directional_score
    score_grid[row][col] = score

    return score


def calculate_scenic_score_for_direction(grid, row_slice, col_slice, target_tree_height, is_toward_southeast):
    score = 0
    if is_toward_southeast:
        for row in range(row_slice[0], row_slice[1]):
            for col in range(col_slice[0], col_slice[1]):
                score += 1
                if grid[row][col] >= target_tree_height:
                    return score
    else:
        for row in reversed(range(row_slice[0], row_slice[1])):
            for col in reversed(range(col_slice[0], col_slice[1])):
                score += 1
                if grid[row][col] >= target_tree_height:
                    return score

    return score


input_file = "data/input_1.txt"
max_score = 1
with open(input_file) as input_grid:
    grid = []
    for line in input_grid:
        tree_list = list(line.rstrip())
        grid.append(tree_list)

    score_grid = [[0 for tree in range(len(grid[row]))] for row in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            score = calculate_score(row, col, grid, score_grid)
            if score > max_score:
                max_score = score

print(f"the highest scenic score possible is {max_score}")
