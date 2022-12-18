def is_visible(row, col, grid, is_visible_grid):
    target_tree_height = grid[row][col]
    n_rows = len(grid)
    n_cols = len(grid[0])

    # check edge
    is_edge = row == 0 or (row == n_rows - 1) or col == 0 or (col == n_cols - 1)
    if is_edge:
        is_visible_grid[row][col] = 1
        return True

    directions = [
        # North
        {
            "row_slice": [0, row],
            "col_slice": [col, col+1]
        },
        # East
        {
            "row_slice": [row, row+1],
            "col_slice": [col+1, n_cols]
        },
        # South
        {
            "row_slice": [row+1, n_rows],
            "col_slice": [col, col+1]
        },
        # West
        {
            "row_slice": [row, row+1],
            "col_slice": [0, col]
        }
    ]

    for direction in directions:
        if is_visible_from_side(grid, direction["row_slice"], direction["col_slice"], target_tree_height):
            is_visible_grid[row][col] = 1
            return True

    return False


def is_visible_from_side(grid, row_slice, col_slice, target_tree_height):
    for row in range(row_slice[0], row_slice[1]):
        for col in range(col_slice[0], col_slice[1]):
            tree = grid[row][col]
            if int(tree) >= int(target_tree_height):
                return False
    return True


input_file = "data/input_1.txt"
with open(input_file) as input:
    grid = []
    for line in input:
        tree_list = list(line.rstrip())
        grid.append(tree_list)

    is_visible_grid = [[0 for tree in range(len(grid[row]))] for row in range(len(grid))]
    visible_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if is_visible(row, col, grid, is_visible_grid):
                visible_count += 1

print(f"there are a total of {visible_count} visible trees in the forest")
