def parse_input():
    input_file = open('input.txt')

    equations_setup = []

    for line in input_file:
        current_line = []

        for char in line:
            current_line.append(char)

        equations_setup.append(current_line)

    return equations_setup


def build_equations(equations_setup):

    equations = equations_setup[0][:-1]

    # build the numbers for the equations
    for line in equations_setup[1:-1]:
        line = line[:-1]

        for index, char in enumerate(line):
                equations[index] += char

    # put the numbers from the same equation into a list
    structured_equations = []
    current_equation = []

    for element in equations:
        if element.isspace():
            structured_equations.append(current_equation)
            current_equation = []
            continue

        current_equation.append(element)

    structured_equations.append(current_equation)

    # add the operators to the equation lists
    equation_index = 0

    for char in equations_setup[-1]:
        if not char.isspace():
            structured_equations[equation_index].append(char)
            equation_index += 1

    return structured_equations


def solve_equations(equations):

    equation_solutions = []

    for equation in equations:

        if equation[-1] == "+":
            result = 0
            for number in equation[:-1]:
                result += int(number)

        elif equation[-1] == "*":
            result = 1
            for number in equation[:-1]:
                result *= int(number)

        equation_solutions.append(result)
    
    return equation_solutions
        

if __name__ == "__main__":

    print("Solution")

    equations_setup = parse_input()

    equations = build_equations(equations_setup)

    equation_solutions = solve_equations(equations)

    print(sum(equation_solutions))
