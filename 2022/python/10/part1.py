import re

parser_regex = re.compile(r"(\w+)+\s?(-?\d*)?")
CPI = {"noop": 1, "addx": 2}


def part1(input_filepath="../../data/10/input"):
    with open(input_filepath) as f:
        data = f.read()

    cmds = []
    for l in data.splitlines():
        cmd = parser_regex.match(l).groups()
        cmds.append((cmd[0], int(cmd[1] or 0)))

    ss = []
    ss_samples = (20, 60, 100, 140, 180, 220)
    ss_samples_iter = iter(ss_samples)
    next_sample = next(ss_samples_iter)
    regx = 1
    clk = 0
    sampled = False
    try:
        for inst, value in cmds:
            if clk == next_sample:
                ss.append(regx * next_sample)
                sampled = True
            clk += CPI[inst]
            if not sampled and clk >= next_sample:
                ss.append(regx * next_sample)
                sampled = True
            regx += value
            if sampled:
                next_sample = next(ss_samples_iter)
                sampled = False
    except StopIteration:
        pass

    return sum(ss)


if __name__ == "__main__":
    import unittest

    X = 13140
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/10/test_input"), X)

    print(f"The result is {part1()}")
