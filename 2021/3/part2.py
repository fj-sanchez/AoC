import copy
import collections


def part2(input_filepath="input"):
    with open(input_filepath) as f:
        input_lines = f.read().splitlines()

    def reduce_lines(input_lines, bit_criteria):
        lines = copy.copy(input_lines)
        for pos in range(len(lines[0])):
            c = collections.Counter()
            for line in lines:
                c.update(line[pos])
            keep = bit_criteria(c.most_common(2))

            lines = list(filter(lambda l: l[pos] == keep, lines))
            if len(lines) == 1:
                break
        value = int(lines[0], 2)

        return value

    def oxygen_bit_criteria(frequencies):
        (most_common, x), (least_common, y) = frequencies
        if x == y:
            return "1"
        return most_common

    def co2_bit_criteria(frequencies):
        (most_common, x), (least_common, y) = frequencies
        if x == y:
            return "0"
        return least_common

    oxygen = reduce_lines(input_lines, oxygen_bit_criteria)
    co2 = reduce_lines(input_lines, co2_bit_criteria)
    result = oxygen * co2

    return result


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part2("test_input"), 230)

    print(f"The result is {part2()}")
