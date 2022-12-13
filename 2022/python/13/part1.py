from ast import literal_eval
from packet_comparison import elements_in_order


def part1(input_filepath="../../data/13/input"):
    with open(input_filepath) as f:
        data = list(filter(lambda x: x, f.read().splitlines()))

    result = 0
    group = lambda t, n: zip(*[t[i::n] for i in range(n)])
    for index, pair in enumerate(group(data, 2), 1):
        left, right = tuple(map(literal_eval, pair))
        print(f"\n== Pair {index} ==")
        try:
            if elements_in_order(left, right):
                result += index
        except StopIteration:
            result += index

    return result


if __name__ == "__main__":
    import unittest

    X = 13
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/13/test_input"), X)

    print(f"The result is {part1()}")
