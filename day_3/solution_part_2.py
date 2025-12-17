def parse_input():
    lines = open("input.txt")

    banks = []

    for line in lines:
        line = line.strip()
        bank = []

        for char in line:
            bank.append(int(char))

        banks.append(bank)

    return banks


def get_battery_from_bank(bank_range):
    battery = -1
    battery_index = -1

    # find battery
    for index, current_battery in enumerate(bank_range):
        # not using max() because I want to update the index
        if current_battery > battery:
            battery = current_battery
            battery_index = index

    return (battery_index, battery)


def get_batteries_from_bank(bank):
    num_needed_batteries = 12
    starting_index = 0
    batteries = ""

    # limit the bank range after every battery found
    for i in range(num_needed_batteries - 1, -1, -1):
        if i == 0:
            battery_result = get_battery_from_bank(bank[starting_index:])
        else:
            battery_result = get_battery_from_bank(bank[starting_index:-i])
        battery_index = battery_result[0] + starting_index
        battery = battery_result[1]

        starting_index = battery_index + 1 
        batteries += str(battery)

    return int(batteries)


def solution(battery_banks):
    batteries_on = []
    
    for bank in battery_banks:
        batteries = get_batteries_from_bank(bank)

        batteries_on.append(batteries)

    # print(batteries_on)
    return sum(batteries_on)


if __name__ == "__main__":
    print("Solution")

    battery_banks = parse_input()

    # print(battery_banks)

    battery_sum = solution(battery_banks)

    print(battery_sum)
