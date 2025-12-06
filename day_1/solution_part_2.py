def parse_input():
    input_file = open('input.txt')

    password_list = []

    for line in input_file:
        line = list(line.strip())
        
        direction = line[0]
        steps = int(''.join((line[1:])))

        password_list.append((direction, steps))
    
    return password_list


def calculate_password(steps):

    current_dial_number = 50
    solution = 0
    
    for direction, number in steps:
        
        if direction == 'L':
            
            while number > 0:
                number -= 1

                current_dial_number -= 1

                if current_dial_number == 0:
                    solution += 1

                if current_dial_number == -1:
                    current_dial_number = 99

        else:
            while number > 0:
                number -= 1

                current_dial_number += 1

                if current_dial_number == 100:
                    current_dial_number = 0
                    solution += 1


    return solution


if __name__ == "__main__":

    steps = parse_input()

    solution = calculate_password(steps)

    print("Solution:" + str(solution))
