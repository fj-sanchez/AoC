import re
from typing import List

parser_regex = re.compile(r"(\w+)+\s?(-?\d*)?")
CPI = {"noop": 1, "addx": 2}


class CRT:
    HEIGHT: int = 6
    WIDTH: int = 40

    def __init__(self):
        self._state: List[List[str]] = [
            list("_" * CRT.WIDTH) for _ in range(CRT.HEIGHT)
        ]
        self._clk: int = 0
        self._regx: int = 1

    @property
    def state(self) -> List[str]:
        return ["".join(line) for line in self._state]

    @property
    def regx(self) -> int:
        return self._regx

    @regx.setter
    def regx(self, value):
        self._regx = value

    def step(self):
        self._clk = (self._clk + 1) % 240
        cursor_position = (self._clk - 1) % CRT.WIDTH
        self._state[(self._clk - 1) // CRT.WIDTH][cursor_position] = self.pixel()

    def pixel(self):
        char = "."
        cursor_position = (self._clk - 1) % CRT.WIDTH
        if (cursor_position - 1) <= self._regx <= (cursor_position + 1):
            return "#"
        return char

    def __repr__(self):
        screen = ""
        for l in self._state:
            screen += "".join(l) + "\n"
        return screen


def part2(input_filepath="../../data/10/input"):
    with open(input_filepath) as f:
        data = f.read()

    cmds = []
    for l in data.splitlines():
        cmd = parser_regex.match(l).groups()
        cmds.append((cmd[0], int(cmd[1] or 0)))

    crt = CRT()
    cmds_iter = iter(cmds)
    try:
        while True:
            cmd, value = next(cmds_iter)
            for _ in range(CPI[cmd]):
                crt.step()
            crt.regx = crt.regx + value
    except StopIteration:
        print(crt)

    return crt.state


if __name__ == "__main__":
    import unittest

    X = [
        "##..##..##..##..##..##..##..##..##..##..",
        "###...###...###...###...###...###...###.",
        "####....####....####....####....####....",
        "#####.....#####.....#####.....#####.....",
        "######......######......######......####",
        "#######.......#######.......#######.....",
    ]
    tc = unittest.TestCase()
    tc.assertEqual(part2("../../data/10/test_input"), X)

    print(f"The result is {part2()}")
