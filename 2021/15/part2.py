import itertools

from part1 import search_ucs


def part2(input_filepath="input"):
    with open(input_filepath) as f:
        map_section = list(map(lambda l: list(map(int, l.strip())), f.readlines()))

    i_len = len(map_section)
    j_len = len(map_section[0])
    ii_len = i_len * 5
    jj_len = j_len * 5

    map_ = [[0] * jj_len for _ in range(ii_len)]
    for ii, jj in itertools.product(range(ii_len), range(jj_len)):
        i = ii % i_len
        j = jj % j_len
        val = map_section[i][j] + (ii // i_len) + (jj // j_len)
        map_[ii][jj] = val // 10 + val % 10

    return search_ucs(map_)


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part2("test_input"), 315)

    print(f"The result is {part2()}")
