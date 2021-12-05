import collections
import dataclasses
import itertools
import math
import re
from typing import Iterable, Tuple


@dataclasses.dataclass
class CloudLine:
    x1: int
    y1: int
    x2: int
    y2: int

    def linepoints(self) -> Iterable[Tuple[int, int]]:
        if self.x1 != self.x2 and self.y1 != self.y2:
            iter_fun = zip
        else:
            iter_fun = itertools.product
        x_dir = int(math.copysign(1, self.x2 - self.x1))
        x_range = range(self.x1, self.x2 + x_dir, x_dir)

        y_dir = int(math.copysign(1, self.y2 - self.y1))
        y_range = range(self.y1, self.y2 + y_dir, y_dir)
        return ((x, y) for (x, y) in iter_fun(x_range, y_range))


def part2(input_filepath="input"):
    line_expr = r"^(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)$"
    reg = re.compile(line_expr)
    with open(input_filepath) as f:
        data = [re.findall(reg, line)[0] for line in f]
    counts = collections.Counter()
    for line in data:
        cloud_points = list(CloudLine(*map(int, line)).linepoints())
        if cloud_points:
            counts.update(cloud_points)

    return len(
        [
            count_val
            for (_, count_val) in itertools.takewhile(
                lambda count: count[1] >= 2, counts.most_common()
            )
        ]
    )


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part2("test_input"), 12)

    print(f"The result is {part2()}")
