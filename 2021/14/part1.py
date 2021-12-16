import collections


def part1(input_filepath="input"):
    with open(input_filepath) as f:
        data = f.readlines()

    cur_pol = data[0].strip()

    insertion_pairs = {}
    for line in data[2:]:
        line = line.strip()
        insertion_pairs[line[:2]] = line[-1]

    for step in range(10):
        new_pol = ""
        for i in range(len(cur_pol) - 1):
            pair = cur_pol[i : i + 2]
            insertion = insertion_pairs[pair]
            if i == 0:
                new_pol += f"{pair[0]}"
            new_pol += f"{insertion}{pair[1]}"
        cur_pol = new_pol

    counts = collections.Counter(cur_pol)
    most_common = counts.most_common()
    (_, most_common_count) = most_common[0]
    (_, least_common_count) = most_common[-1]

    return most_common_count - least_common_count


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part1("test_input"), 1588)

    print(f"The result is {part1()}")
