import re

from collections import deque


def part2(input_filepath="../../data/5/input"):
    with open(input_filepath) as f:
        data = f.read().splitlines()

    # find separation line between crates initial state and commands
    cmds_start_ix = data.index("")

    # extract crates initial state
    num_stacks = int(data[cmds_start_ix - 1].split()[-1])
    stacks = {i: deque() for i in range(1, num_stacks + 1)}
    for i, stack in stacks.items():
        col = ((i - 1) * 4) + 1
        for row in reversed(data[: cmds_start_ix - 1]):
            if len(row) < col:
                continue
            if row[col] != " ":
                stack.append(row[col])

    # extract commands

    cmd_regex = re.compile(r".*?(\d+).*?(\d+).*?(\d+)")
    for cmd in data[cmds_start_ix + 1 :]:
        repeat, ori, dest = map(int, re.findall(cmd_regex, cmd)[0])
        stacks[dest].extend(reversed([stacks[ori].pop() for _ in range(repeat)]))

    return "".join([s[-1] for s in stacks.values()])


if __name__ == "__main__":
    import unittest

    X = "MCD"
    tc = unittest.TestCase()
    tc.assertEqual(part2("../../data/5/test_input"), X)

    print(f"The result is {part2()}")
