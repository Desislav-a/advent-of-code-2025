from functools import lru_cache

def get_starting_point_of_laser():
    input_file = open('input.txt')

    starting_point = -1

    for line in input_file:
        for index, char in enumerate(line):
            if char == "S":
                starting_point = index
        break
    
    return starting_point


def build_matrix_from_input():
    input_file = open('input.txt')

    grid = []

    for line in input_file:
        current_row = []

        for char in line:
            current_row.append(char)
        
        grid.append(current_row)
            
    return grid


def solution(starting_point: int, grid: list[list[str]]) -> int:
    seen_splitters = set()
    to_visit = [(0, starting_point)]

    while to_visit:
        current_row, current_column = to_visit.pop()

        for index, row in enumerate(grid[current_row + 1:]):
            index = index + current_row + 1
            
            if row[current_column] == "^":
                if (index, current_column) not in seen_splitters: 
                    seen_splitters.add((index, current_column))

                    if current_column - 1 >= 0:
                        to_visit.append((index, current_column - 1)) #left
                    
                    if current_column + 1 < len(row) - 1:  #right
                        to_visit.append((index, current_column + 1))
                
                break
    
    # print(len(seen_splitters))
                    
    return len(seen_splitters)


@lru_cache
def count_timeline(starting_point, grid):

    all_paths = []
    number_of_rows = len(grid)
    number_of_columns = len(grid[0])

    def depth_first_traversal(current_location, current_path):
        current_row, current_column = current_location

        # print((current_row, current_column))

        if current_row == number_of_rows - 1:
            all_paths.append(current_path)
            return
        
        if grid[current_row][current_column] == "^":
            if current_column - 1 >= 0: # left
                depth_first_traversal((current_row + 1, current_column - 1), current_path)

            if current_column + 1 < number_of_columns - 1:  # right
                depth_first_traversal((current_row + 1, current_column + 1), current_path)
        else:
            current_path.append((current_row, current_column))
            depth_first_traversal((current_row + 1, current_column), current_path)
                

    depth_first_traversal((0, starting_point), [])

    # for element in all_paths:
    #     print(element)

    return len(all_paths)

if __name__ == "__main__":

    print("Solution")

    starting_point = get_starting_point_of_laser()

    grid = build_matrix_from_input()

    # print(starting_point)

    # for row in grid:
    #     print(row)

    result = solution(starting_point, grid)

    print(result)

    print(count_timeline(starting_point, grid))
