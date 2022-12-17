from collections import namedtuple
from dataclasses import dataclass
from typing import Tuple

XY = namedtuple("XY", ["x", "y"])


@dataclass
class SandGrain:
    x: int
    y: int


def parse_input(input_filepath):
    with open(input_filepath) as f:
        path_definitions = [
            tuple(map(lambda x: tuple(map(int, x.split(","))), line.split(" ->")))
            for line in f.read().splitlines()
        ]
    paths = list()
    for path in path_definitions:
        path_coords = set()
        for (ax, ay), (bx, by) in zip(path[:-1], path[1:]):
            if ax == bx:
                if ay < by:
                    path_coords.update({(ax, y) for y in range(ay, by + 1)})
                else:
                    path_coords.update({(ax, y) for y in range(by, ay + 1)})
            elif ay == by:
                if ax < bx:
                    path_coords.update({(x, ay) for x in range(ax, bx + 1)})
                else:
                    path_coords.update({(x, ay) for x in range(bx, ax + 1)})
        paths.append(path_coords)
    return paths


class Grid:
    START = XY(500, 0)

    def __init__(self, paths):
        y_ = [y for path in paths for x, y in path] + [Grid.START.y]
        self.min_y = min(y_)
        self.max_y = max(y_)
        x_ = [x for path in paths for x, y in path] + [Grid.START.x]
        self.min_x = min(x_)
        self.max_x = max(x_)
        self.span_x = self.max_x - self.min_x + 1
        self.span_y = self.max_y - self.min_y + 1
        self.start = XY(Grid.START.x - self.min_x, Grid.START.y - self.min_y)

        self._state = [["." for _ in range(self.span_x)] for _ in range(self.span_y)]

        for path in paths:
            for x, y in path:
                self._state[y - self.min_y][x - self.min_x] = "#"
        self._state[self.start.y][self.start.x] = "+"

    def in_bounds(self, x, y):
        return 0 <= x < self.span_x and 1 <= y < self.span_y

    def move(self, sand: SandGrain) -> Tuple[bool, bool]:
        moved = True
        fall_off = False
        _sand_x, _sand_y = sand.x, sand.y

        if not self.in_bounds(_sand_x, _sand_y + 1):
            fall_off = True
        elif self._state[_sand_y + 1][_sand_x] == ".":
            _sand_y += 1
        elif not self.in_bounds(_sand_x - 1, _sand_y + 1):
            fall_off = True
        elif self._state[_sand_y + 1][_sand_x - 1] == ".":
            _sand_y += 1
            _sand_x -= 1
        elif not self.in_bounds(_sand_x + 1, _sand_y + 1):
            fall_off = True
        elif self._state[_sand_y + 1][_sand_x + 1] == ".":
            _sand_y += 1
            _sand_x += 1
        else:
            moved = False

        if moved:
            self._state[sand.y][sand.x] = "."
            if not fall_off:
                self._state[_sand_y][_sand_x] = "o"
                sand.x = _sand_x
                sand.y = _sand_y
        return moved, fall_off

    def produce_sand(self):
        if self._state[self.start.y][self.start.x] != "o":
            self._state[self.start.y][self.start.x] = "o"
            return SandGrain(self.start.x, self.start.y)
        return None

    def __repr__(self):
        return "\n".join(["".join(row) for row in self._state])

    def print(self):
        print("\033[H\033[J", end="")
        print(self)


class Grid2(Grid):
    def __init__(self, paths):
        y_ = [y for path in paths for x, y in path] + [Grid.START.y]
        self.min_y = min(y_)
        self.max_y = max(y_) + 2
        self.span_y = self.max_y - self.min_y + 1
        floor_width = (self.span_y - 2) * 2 + 3

        floor_path_definition = (
            XY(Grid2.START.x - (floor_width - 1) // 2, self.max_y),
            XY(Grid2.START.x + (floor_width - 1) // 2, self.max_y),
        )
        (ax, ay), (bx, by) = floor_path_definition
        floor_path = {(x, ay) for x in range(ax, bx + 1)}

        x_ = [x for path in paths + [floor_path] for x, y in path] + [Grid.START.x]
        self.min_x = min(x_)
        self.max_x = max(x_)
        self.span_x = self.max_x - self.min_x + 1
        self.start = XY(Grid.START.x - self.min_x, Grid.START.y - self.min_y)

        self._state = [["." for _ in range(self.span_x)] for _ in range(self.span_y)]

        for path in paths + [floor_path]:
            for x, y in path:
                self._state[y - self.min_y][x - self.min_x] = "#"
        self._state[self.start.y][self.start.x] = "+"
