from collections import namedtuple
from typing import Any, Optional, List, Set

XY = namedtuple("XY", ("x", "y"))

CMD_TO_DIFF = {"U": XY(0, 1), "R": XY(1, 0), "D": XY(0, -1), "L": XY(-1, 0)}
DIFF_TO_CMDS = {
    # overlap
    (0, 0): None,
    # adjacent
    (0, 1): None,
    (0, -1): None,
    (1, 1): None,
    (1, 0): None,
    (1, -1): None,
    (-1, 1): None,
    (-1, 0): None,
    (-1, -1): None,
    # non-adjacent
    (2, 2): XY(1, 1),
    (2, 1): XY(1, 1),
    (2, 0): XY(1, 0),
    (2, -1): XY(1, -1),
    (2, -2): XY(1, -1),
    (-2, 2): XY(-1, 1),
    (-2, 1): XY(-1, 1),
    (-2, 0): XY(-1, 0),
    (-2, -1): XY(-1, -1),
    (-2, -2): XY(-1, -1),
    (1, 2): XY(1, 1),
    (1, -2): XY(1, -1),
    (0, 2): XY(0, 1),
    (0, -2): XY(0, -1),
    (-1, 2): XY(-1, 1),
    (-1, -2): XY(-1, -1),
}


class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self._x = x
        self._y = y

    @property
    def pos(self):
        return XY(self._x, self._y)

    def dist(self, target: "Point") -> int:
        diff = self - target
        return abs(diff.x) + abs(diff.y)

    def __sub__(self, other: Any) -> XY:
        if not isinstance(other, Point):
            raise ValueError()
        return self.pos.x - other.pos.x, self.pos.y - other.pos.y

    def move(self, xy: Optional[XY]) -> None:
        if xy is None:
            return
        self._x += xy.x
        self._y += xy.y


def print_knots(head: Point, knots: List[Point]):
    screen = [list("..........................") for _ in range(21)]
    screen[head.pos.y][head.pos.x] = "H"
    for i, knot in enumerate(knots):
        if screen[knot.pos.y][knot.pos.x] != ".":
            break
        screen[knot.pos.y][knot.pos.x] = str(i + 1)

    for l in reversed(screen):
        print("".join(l))
    print("")


def print_visited(visited: Set[XY]):
    screen = [list("..........................") for _ in range(21)]
    for p in visited:
        screen[p.y][p.x] = "#"

    for l in reversed(screen):
        print("".join(l))
    print("")
