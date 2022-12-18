from collections import deque, namedtuple

import numpy as np
from dataclasses import dataclass


@dataclass(frozen=True)
class Pixel:
    x: int
    y: int
    z: int


class Grid:
    DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

    def __init__(self, pixels):
        x_ = [pixel.x for pixel in pixels]
        self.x_max = max(x_)
        self.x_min = min(x_)
        self.x_span = self.x_max - self.x_min + 3

        y_ = [pixel.y for pixel in pixels]
        self.y_max = max(y_)
        self.y_min = min(y_)
        self.y_span = self.y_max - self.y_min + 3

        z_ = [pixel.z for pixel in pixels]
        self.z_max = max(z_)
        self.z_min = min(z_)
        self.z_span = self.z_max - self.z_min + 3

        self._grid = self._grid = np.zeros(
            (self.x_span, self.y_span, self.z_span), dtype=int
        )

        self.exposed_sides = 0

    def insert_pixels(self, pixels):
        for pixel in pixels:
            p = XYZ(
                pixel.x - self.x_min + 1,
                pixel.y - self.y_min + 1,
                pixel.z - self.z_min + 1,
            )
            self._grid[p.x][p.y][p.z] = 1
            self.exposed_sides += 6
            for dir_x, dir_y, dir_z in Grid.DIRS:
                if self._grid[p.x + dir_x][p.y + dir_y][p.z + dir_z]:
                    self.exposed_sides -= 2


XYZ = namedtuple("XYZ", ["x", "y", "z"])


class Grid2(Grid):
    def insert_pixels(self, pixels):
        for p in pixels:
            self._grid[p.x - self.x_min + 1][p.y - self.y_min + 1][
                p.z - self.z_min + 1
            ] = 1

        explored = set()
        frontier = deque()
        start = XYZ(0, 0, 0)
        frontier.append(start)
        explored.add(start)
        while frontier:
            coord = frontier.pop()
            for dir_x, dir_y, dir_z in Grid.DIRS:
                neighbour = XYZ(coord.x + dir_x, coord.y + dir_y, coord.z + dir_z)
                if self.inbounds(neighbour) and neighbour not in explored:
                    if self._grid[neighbour.x, neighbour.y, neighbour.z]:
                        self.exposed_sides += 1
                    else:
                        explored.add(neighbour)
                        frontier.append(neighbour)

    def inbounds(self, p: XYZ):
        return (
            (0 <= p.x < self.x_span)
            and (0 <= p.y < self.y_span)
            and (0 <= p.z < self.z_span)
        )
