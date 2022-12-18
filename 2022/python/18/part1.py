from grid import Pixel, Grid


def part1(input_filepath="../../data/18/input"):
    with open(input_filepath) as f:
        data = f.read().splitlines()

    pixels = tuple(Pixel(*tuple(map(int, line.split(",")))) for line in data)
    grid = Grid(pixels)
    grid.insert_pixels(pixels)

    return grid.exposed_sides


if __name__ == "__main__":
    import unittest

    X = 64
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/18/test_input"), X)

    print(f"The result is {part1()}")
