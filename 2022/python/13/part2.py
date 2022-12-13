from ast import literal_eval
from functools import cmp_to_key
from packet_comparison import compare_packets


def part2(input_filepath="../../data/13/input"):
    with open(input_filepath) as f:
        data = list(map(literal_eval, filter(lambda x: x, f.read().splitlines())))
    MARKER_1 = [[2]]
    MARKER_2 = [[6]]
    data.append(MARKER_1)
    data.append(MARKER_2)

    ordered_group = list(sorted(data, key=cmp_to_key(compare_packets)))
    return (ordered_group.index(MARKER_1) + 1) * (ordered_group.index(MARKER_2) + 1)


if __name__ == "__main__":
    import unittest

    X = 140
    tc = unittest.TestCase()
    tc.assertEqual(part2("../../data/13/test_input"), X)

    print(f"The result is {part2()}")
