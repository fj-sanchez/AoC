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


def part2(input_filepath="../../data/7/input"):
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

    unused = 70000000 - dir_sizes[""]
    t = sorted(
        filter(
            lambda x: unused + x >= 30000000,
            dir_sizes.values(),
        )
    )
    return t[0]


if __name__ == "__main__":
    import unittest

    X = 24933642
    tc = unittest.TestCase()
    tc.assertEqual(part2("../../data/7/test_input"), X)

    print(f"The result is {part2()}")
