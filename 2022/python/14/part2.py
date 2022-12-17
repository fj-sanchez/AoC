from grid import parse_input, Grid2


def part2(input_filepath="../../data/14/input"):
    paths = parse_input(input_filepath)

    grid = Grid2(paths)
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

    return sand_count


if __name__ == "__main__":
    import unittest

    X = 93
    tc = unittest.TestCase()
    tc.assertEqual(part2("../../data/14/test_input"), X)

    print(f"The result is {part2()}")
