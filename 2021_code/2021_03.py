import aocd


def part_one(in_list):
    delta_bits = []
    for pos in zip(*in_list):
        if pos.count("1") > pos.count("0"):
            delta_bits.append("1")
        else:
            delta_bits.append("0")
    delta = int("".join(delta_bits), 2)
    eps = ~delta & 2 ** len(in_list[0]) - 1
    return delta * eps


def part_two(in_list):
    ox = int(get_rating(in_list, 0, "1")[0], 2)
    co2 = int(get_rating(in_list, 0, "0")[0], 2)
    return ox * co2


def get_rating(in_list, pos, val_for_more_ones):
    if len(in_list) == 1:
        return in_list
    other_val = list({"0", "1"}.difference({val_for_more_ones}))[0]
    pos = pos % len(in_list[0])
    bits_in_pos = [line[pos] for line in in_list]
    if bits_in_pos.count("1") >= bits_in_pos.count("0"):
        new_data = [line for line in in_list if line[pos] == val_for_more_ones]
    else:
        new_data = [line for line in in_list if line[pos] == other_val]
    return get_rating(new_data, pos + 1, val_for_more_ones)


input_list = aocd.get_data(day=3, year=2021).splitlines()
print('1:', part_one(input_list))
print('2:', part_two(input_list))