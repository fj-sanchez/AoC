import operator
import collections


def part1(input_filepath="input"):
    with open(input_filepath) as f:
        lines = f.read().splitlines()
        one_counts = [collections.Counter() for _ in lines[0]]
        _ = {one_counts[i].update(bit) for line in lines for i, bit in enumerate(line)}

        result_codes = {"gamma": "", "epsilon": ""}
        for counter in one_counts:
            (gamma_bit, _), (epsilon_bit, _) = counter.most_common(2)
            result_codes["gamma"] += gamma_bit
            result_codes["epsilon"] += epsilon_bit

        result = int(result_codes["gamma"], 2) * int(result_codes["epsilon"], 2)

    return result


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part1("test_input"), 198)

    print(f"The result is {part1()}")
