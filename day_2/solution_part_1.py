def parse_input():
    input_file = open('input.txt')

    ranges = []

    for line in input_file:
        line = line.strip()
        temp_ranges = line.split(",")

        for current_range in temp_ranges:
            current_range_split = current_range.split("-")

            left_limit = current_range_split[0]
            right_limit = current_range_split[1]

            ranges.append((int(left_limit), int(right_limit)))
    
    return ranges


def check_ID_is_valid(current_id):
    
    current_id = str(current_id)

    if len(current_id) % 2 != 0:
        return True
    else:

        left_side_id = current_id[:len(current_id)//2]
        right_side_id = current_id[len(current_id)//2:]

        if left_side_id == right_side_id:
            return False

    return True


def find_invalid_IDs(ranges):

    invalid_IDs = []

    for left_limit, right_limit in ranges:
        
        for i in range(left_limit, right_limit + 1):
            if not check_ID_is_valid(i):
                invalid_IDs.append(i)

    return invalid_IDs
    

if __name__ == "__main__":

    print("Solution")

    ranges = parse_input()

    invalid_IDs = find_invalid_IDs(ranges)

    print(sum(invalid_IDs))
