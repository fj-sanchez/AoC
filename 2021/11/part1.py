import itertools


def part1(input_filepath="input"):
    with open(input_filepath) as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]

    max_i = len(data)
    max_j = len(data)

    def adjacent(i, j):
        for (di, dj) in itertools.product([-1, 0, 1], [-1, 0, 1]):
            if di == dj == 0:
                continue
            a_i, a_j = i + di, j + dj
            if 0 <= a_i < max_i and 0 <= a_j < max_j:
                yield a_i, a_j

    flashes = 0
    for step in range(100):
        has_flashed_this_step = [[False for _ in range(max_j)] for _ in range(max_i)]
        for i, j in itertools.product(range(max_i), range(max_j)):
            data[i][j] += 1

        keep_checking = True
        while keep_checking:
            keep_checking = False
            for i, j in itertools.product(range(max_i), range(max_j)):
                if data[i][j] > 9 and not has_flashed_this_step[i][j]:
                    keep_checking |= True
                    has_flashed_this_step[i][j] = True
                    for (adj_i, adj_j) in adjacent(i, j):
                        data[adj_i][adj_j] += 1
        flashes += sum(sum(int(x) for x in line) for line in has_flashed_this_step)
        for i, j in itertools.product(range(max_i), range(max_j)):
            if has_flashed_this_step[i][j]:
                data[i][j] = 0

    return flashes


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part1("test_input"), 1656)

    print(f"The result is {part1()}")
