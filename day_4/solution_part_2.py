def build_grid_from_input():
    lines = open("input.txt")

    grid = []

    for line in lines:
        line = line.strip()
        
        current_row = []

        for char in line:
            current_row.append(char)

        grid.append(current_row)

    return grid


def can_access_paper_roll(paper_roll_location, grid):
    current_row = paper_roll_location[0]
    current_column = paper_roll_location[1]

    num_neighbours = 0

    # north
    if current_row != 0:
        if grid[current_row - 1][current_column] == "@":
            num_neighbours += 1
    
    # northwest
    if current_row != 0 and current_column != 0:
        if grid[current_row - 1][current_column - 1] == "@":
            num_neighbours += 1
    
    # northeast
    if current_row != 0 and current_column < len(grid[0]) - 1:
        if grid[current_row - 1][current_column + 1] == "@":
            num_neighbours += 1

    # west
    if current_column != 0:
        if grid[current_row][current_column - 1] == "@":
            num_neighbours += 1

    # east
    if current_column < len(grid[0]) - 1:
        if grid[current_row][current_column + 1] == "@":
            num_neighbours += 1

    # south
    if current_row != len(grid) - 1:
        if grid[current_row + 1][current_column] == "@":
            num_neighbours += 1
    
    # southwest
    if current_row != len(grid) - 1 and current_column != 0:
        if grid[current_row + 1][current_column - 1] == "@":
            num_neighbours += 1
    
    # northeast
    if current_row != len(grid) - 1 and current_column < len(grid[0]) - 1:
        if grid[current_row + 1][current_column + 1] == "@":
            num_neighbours += 1


    if num_neighbours < 4:
        grid[current_row][current_column] = "."
        return True

    return False


def solution(grid):
    accessible_paper_role = 0
    
    for row_index, row in enumerate(grid):
        for paper_roll_index, paper_roll in enumerate(grid[row_index]):
            # check if it's paper roll
            if grid[row_index][paper_roll_index] == "@":
                if can_access_paper_roll((row_index, paper_roll_index), grid):
                    accessible_paper_role += 1

    return accessible_paper_role


if __name__ == "__main__":
    print("Solution")

    grid = build_grid_from_input()

    total_sum = 0
   
    result = solution(grid)
    total_sum += result

    # whilst there are still paper rolls to be moved, continue
    while result != 0:
        result = solution(grid)
        total_sum += result

    print(total_sum)

   
