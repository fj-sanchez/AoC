import functools
import collections


def part2(input_filepath="input"):
    with open(input_filepath) as f:
        data = f.readlines()

    cur_pol = data[0].strip()

    insertion_pairs = {}
    for line in data[2:]:
        line = line.strip()
        insertion_pairs[line[:2]] = line[-1]

    @functools.lru_cache
    def resolve_pair(pair):
        new_ = insertion_pairs[pair]
        return pair[0] + new_, new_ + pair[1]

    counts = collections.Counter()
    for i in range(len(cur_pol) - 1):
        pair = cur_pol[i : i + 2]
        counts.update((pair,))

    letter_count = collections.Counter(cur_pol)
    for step in range(40):
        new_counts = collections.Counter()
        for pair, count in counts.items():
            letter = insertion_pairs[pair]
            letter_count[letter] += count

            l, r = resolve_pair(pair)
            new_counts[l] += count
            new_counts[r] += count
        counts = new_counts

    most_common = letter_count.most_common()
    (_, most_common_count) = most_common[0]
    (_, least_common_count) = most_common[-1]

    return most_common_count - least_common_count


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part2("test_input"), 2188189693529)

    print(f"The result is {part2()}")
