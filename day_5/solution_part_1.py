def build_fresh_product_ranges():
    lines = open("input.txt")

    ranges = []

    for line in lines:
        line = line.strip()

        if line == "":
            break
        
        parsed_line = line.split("-")
        ranges.append([int(parsed_line[0]), int(parsed_line[1])])

    return ranges


def optimise_fresh_ranges(ranges):
    ranges.sort(key =lambda x: x[0])

    optimised_fresh_ranges = [ranges[0]]

    for current_range in ranges[1:]:
        range_left_side = current_range[0]
        range_right_side = current_range[1]

        if range_left_side > optimised_fresh_ranges[-1][0] and range_left_side < optimised_fresh_ranges[-1][1]:
            optimised_fresh_ranges[-1][1] = range_right_side
        else:
            optimised_fresh_ranges.append(current_range)

    return optimised_fresh_ranges


def get_products():
    lines = open("input.txt")
    products = []

    is_product = False

    for line in lines:
        line = line.strip()

        if line == "":
            is_product = True
            continue

        if is_product:
            products.append(int(line))

    return products


def get_fresh_products(fresh_ranges, products):

    fresh_products = []

    for product in products:
        for current_range in fresh_ranges:

            range_left_side = current_range[0]
            range_right_side = current_range[1]

            if product >= range_left_side and product <= range_right_side:
                fresh_products.append(product)


    return fresh_products


if __name__ == "__main__":
    print("Solution")

    fresh_ranges = build_fresh_product_ranges()

    # print("Initial ranges")
    # print(fresh_ranges)

    optimised_fresh_ranges = optimise_fresh_ranges(fresh_ranges)

    # print("Optimised ranges")
    # print(optimised_fresh_ranges)

    products = get_products()

    # print(products)

    fresh_products = get_fresh_products(optimised_fresh_ranges, products)

    print(fresh_products)
    print(len(fresh_products))

    
    # 672 - too low - with break
    # 757 - too high - no break
  
