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


def get_batteries_from_bank(bank):
    first_battery = -1
    first_battery_index = -1

    second_battery = -1

    # find first battery
    for index, battery in enumerate(bank[:-1]):
        # not using max() because I want to update the index
        if battery > first_battery:
            first_battery = battery
            first_battery_index = index

    # find second battery 
    for battery in bank[first_battery_index + 1:]:
        second_battery = max(battery, second_battery)

    return int(str(first_battery) + str(second_battery))


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
