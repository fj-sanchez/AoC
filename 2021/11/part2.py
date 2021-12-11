import itertools


def part2(input_filepath="input"):
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

    first_sync_flash = -1
    step = 0
    while first_sync_flash < 0:
        step += 1
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
        if (
            sum(sum(int(x) for x in line) for line in has_flashed_this_step)
            == max_i * max_j
        ):
            first_sync_flash = step
            break

        for i, j in itertools.product(range(max_i), range(max_j)):
            if has_flashed_this_step[i][j]:
                data[i][j] = 0

    return first_sync_flash


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part2("test_input"), 195)

    print(f"The result is {part2()}")
