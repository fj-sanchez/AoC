import functools
import operator


def basin_floodfill(data, point_pos, basin=None):
    max_i = len(data)
    max_j = len(data[0])
    if basin is None:
        basin = [[0 for _ in range(max_j)] for _ in range(max_i)]
        assert len(basin) == len(data)
        assert len(basin[0]) == len(data[0])

    i, j = point_pos
    point = data[i][j]
    if point >= 9:
        return basin

    if not basin[i][j]:
        basin[i][j] = 1
        # up
        if i > 0 and data[i - 1][j] > point:
            basin_point = (i - 1, j)
            basin_floodfill(data, basin_point, basin)
        # down
        if i < max_i - 1 and data[i + 1][j] > point:
            basin_point = (i + 1, j)
            basin_floodfill(data, basin_point, basin)
        # left
        if j > 0 and data[i][j - 1] > point:
            basin_point = (i, j - 1)
            basin_floodfill(data, basin_point, basin)
        # right
        if j < max_j - 1 and data[i][j + 1] > point:
            basin_point = (i, j + 1)
            basin_floodfill(data, basin_point, basin)
    return basin


def part2(input_filepath="input"):
    with open(input_filepath) as f:
        data = [[int(p) for p in line.strip()] for line in f.readlines()]

    low_points = []
    for i, col in enumerate(data):
        for j, point in enumerate(col):
            if i > 0 and data[i - 1][j] <= point:
                continue
            if i < len(data) - 1 and data[i + 1][j] <= point:
                continue
            if j > 0 and data[i][j - 1] <= point:
                continue
            if j < len(col) - 1 and data[i][j + 1] <= point:
                continue
            low_points.append((i, j))

    basin_sizes = []
    for low_point in low_points:
        size = sum(sum(row) for row in basin_floodfill(data, low_point))
        basin_sizes.append(size)

    top_3_basins = sorted(basin_sizes, reverse=True)[:3]
    result = functools.reduce(operator.mul, top_3_basins)

    return result


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part2("test_input"), 1134)

    print(f"The result is {part2()}")
