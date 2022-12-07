from collections import defaultdict
from string import digits


class CWD:
    def __init__(self):
        self.cwd = ""

    def cd(self, dir_):
        if dir_ == "..":
            self.cwd = self.cwd.rsplit("/", 1)[0]
        elif dir_ == "/":
            self.cwd = "/"
        else:
            self.cwd += f"/{dir_}" if self.cwd != "/" else dir_

    def directories(self):
        if self.cwd == "/":
            yield ""
        else:
            tmp = self.cwd.rsplit("/")
            while tmp:
                yield "".join(tmp)
                tmp.pop()

    def get(self):
        return self.cwd


def part1(input_filepath="../../data/7/input"):
    with open(input_filepath) as f:
        data = f.read().splitlines()

    dir_sizes = defaultdict(int)
    cwd = CWD()
    for line in data:
        if line.startswith("$ cd"):
            cwd.cd(line[5:])
        elif line[0] in digits:
            file_size = int(line.split()[0])
            for dir in cwd.directories():
                dir_sizes[dir] += file_size

    return sum(filter(lambda x: x < 100000, dir_sizes.values()))


if __name__ == "__main__":
    import unittest

    X = 95437
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/7/test_input"), X)

    print(f"The result is {part1()}")
