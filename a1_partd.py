#    Main Author(s): Hargun, Jagbir Singh
#    Main Reviewer(s):


from a1_partc import Queue

def get_overflow_list(grid):
    rows, cols = len(grid), len(grid[0])
    overflow_cells = []

    for row in range(rows):
        for col in range(cols):
            num_neighbors = 4  # Default for inner cells
            if row == 0 or row == rows - 1:
                num_neighbors -= 1
            if col == 0 or col == cols - 1:
                num_neighbors -= 1

            cell_value = abs(grid[row][col])
            if cell_value >= num_neighbors:
                overflow_cells.append((row, col))

    return overflow_cells if overflow_cells else None 

def overflow(grid, a_queue):
    overflow_cells = get_overflow_list(grid)

    if not overflow_cells:
        return 0  # No overflowing cells or all have same sign

    # Check if all non-zero cells have the same sign
    if all(value < 0 for row in grid for value in row if value) or all(value > 0 for row in grid for value in row if value):
        return 0
    
    sign = []
    for row, col in overflow_cells: # Set Overflow cells to 0
        if grid[row][col] > 0: # Determine overflow sign
            sign.append(1)
        else:
            sign.append(-1)  
        grid[row][col] = 0 

    for i, (row, col) in enumerate(overflow_cells):
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = row + dx, col + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                grid[x][y] = (abs(grid[x][y]) + 1) * sign[i] # Increment neighouring cells by 1 and set the sign to overflow
    
    a_queue.enqueue([row[:] for row in grid])

    return 1 + overflow(grid, a_queue)  # Recursive call
