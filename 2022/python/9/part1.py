from typing import Set

from _point import Point, XY, CMD_TO_DIFF, DIFF_TO_CMDS


def part1(input_filepath="../../data/9/input"):
    with open(input_filepath) as f:
        input_data = f.read()

    def parse(line):
        tmp = line.split()
        return tmp[0], int(tmp[1])

    input_data = map(parse, input_data.splitlines())
    head = Point()
    tail = Point()
    visited: Set[XY] = {XY(0, 0)}
    for (cmd, reps) in input_data:
        for _ in range(reps):
            head.move(CMD_TO_DIFF[cmd])
            tail.move(DIFF_TO_CMDS[head - tail])
            visited.add(tail.pos)

    return len(visited)


if __name__ == "__main__":
    import unittest

    X = 13
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/9/test_input"), X)

    print(f"The result is {part1()}")
