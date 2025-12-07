def _initialise_equations():
    input_file = open('input.txt')

    for line in input_file:
        number_of_equations = line.strip().split()
        break

    return [[] for _ in range(len(number_of_equations))]


def parse_input():
    input_file = open('input.txt')

    equations = _initialise_equations()

    for line in input_file:
        equation_elements = line.strip().split()

        for index, element in enumerate(equation_elements):
            equations[index].append(element)
        
    return equations


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

    equations = parse_input()

    # print(equations)

    equation_solutions = solve_equations(equations)

    # print(equation_solutions)

    print(sum(equation_solutions))
