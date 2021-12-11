def part1(input_filepath="input"):
    with open(input_filepath) as f:
        data = [[int(p) for p in line.strip()] for line in f.readlines()]

    low_points = []
    for i, col in enumerate(data):
        for j, point in enumerate(col):
            if i > 0 and data[i - 1][j] <= point:
                continue
            if i < len(data)-1 and data[i + 1][j] <= point:
                continue
            if j > 0 and data[i][j - 1] <= point:
                continue
            if j < len(col)-1 and data[i][j + 1] <= point:
                continue
            low_points.append(point + 1)

    return sum(low_points)


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part1("test_input"), 15)

    print(f"The result is {part1()}")
