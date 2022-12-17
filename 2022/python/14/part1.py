from time import sleep

from grid import parse_input, Grid


def part1(input_filepath="../../data/14/input"):
    paths = parse_input(input_filepath)

    grid = Grid(paths)
    sand_count = 0
    fall_off = False
    # grid.print()
    while (sand := grid.produce_sand()) and not fall_off:
        moved = True
        while moved and not fall_off:
            moved, fall_off = grid.move(sand)
            # grid.print()
        if not fall_off:
            sand_count += 1
        # grid.print()
        # sleep(0.1)

    return sand_count


if __name__ == "__main__":
    import unittest

    X = 24
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/14/test_input"), X)

    print(f"The result is {part1()}")
