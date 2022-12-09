from typing import Set

from _point import Point, XY, CMD_TO_DIFF, DIFF_TO_CMDS


def part2(input_filepath="../../data/9/input"):
    with open(input_filepath) as f:
        input_data = f.read()

    def parse(line):
        tmp = line.split()
        return tmp[0], int(tmp[1])

    input_data = map(parse, input_data.splitlines())
    head = Point()
    knots = [Point() for _ in range(9)]
    visited: Set[XY] = {XY(0, 0)}

    for (cmd, reps) in input_data:
        for _ in range(reps):
            head.move(CMD_TO_DIFF[cmd])
            for a, b in zip(knots, [head] + knots[:-1]):
                a.move(DIFF_TO_CMDS[b - a])
            visited.add(knots[-1].pos)

    return len(visited)


if __name__ == "__main__":
    import unittest

    X = 36
    tc = unittest.TestCase()
    tc.assertEqual(part2("../../data/9/test_input2"), X)

    print(f"The result is {part2()}")
