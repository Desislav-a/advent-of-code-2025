def parse_input():
    input_file = open('input.txt')

    password_list = []

    for line in input_file:
        line = list(line.strip())
        
        direction = line[0]
        steps = int(''.join((line[1:])))

        password_list.append((direction, steps))
    
    return password_list

    
def generate_dial(dial_size: int) -> list[int]:
    return [i for i in range(dial_size)]


def calculate_password(steps, safe_dial_numbers):

    current_dial_number = 50
    solution = 0
    
    for direction, number in steps:
        
        if direction == 'L':
            if number <= current_dial_number:
                current_dial_number = current_dial_number - number
            else:
                number = number - current_dial_number

                while number > len(safe_dial_numbers) - 1:
                    number = number - len(safe_dial_numbers)

                current_dial_number = safe_dial_numbers[-number]
    
        else:
            if number + current_dial_number <= len(safe_dial_numbers) - 1:
                current_dial_number = current_dial_number + number
            else:
                number = number + current_dial_number - len(safe_dial_numbers)

                while number > len(safe_dial_numbers) - 1:
                    number = number - len(safe_dial_numbers)

                current_dial_number = safe_dial_numbers[number]

        if current_dial_number == 0:
            solution+= 1

    return solution


if __name__ == "__main__":

    steps = parse_input()

    safe_dial_numbers = generate_dial(100)

    solution = calculate_password(steps, safe_dial_numbers)

    print("Solution:" + str(solution))
