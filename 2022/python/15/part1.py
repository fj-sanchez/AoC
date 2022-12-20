from collections import defaultdict
from typing import List, Dict, Set
from common import parse_input, compact, XSPAN, XY

ROWS_OF_INTEREST = iter((10, 2000000))


def part1(input_filepath="../../data/15/input"):
    with open(input_filepath) as f:
        data = f.readlines()

    row_of_interest = next(ROWS_OF_INTEREST)

    sensors = parse_input(data)
    rows: Dict[int, List[XSPAN]] = defaultdict(list)
    blocked_coords: Set[XY] = set()
    for sensor in sensors:
        # avoid using spaces used by sensors or beacons
        sensor_coord = XY(sensor.x, sensor.y)
        beacon_coord = XY(sensor.beacon_x, sensor.beacon_y)
        blocked_coords.add(sensor_coord)
        blocked_coords.add(beacon_coord)

        dist = abs(sensor.x - sensor.beacon_x) + abs(sensor.y - sensor.beacon_y)

        if (
            sensor.y <= row_of_interest <= sensor.y + dist
            or sensor.y - dist <= row_of_interest <= sensor.y
        ):
            dx = dist - abs(sensor.y - row_of_interest)
            rows[row_of_interest].append(XSPAN(sensor.x - dx, sensor.x + dx + 1))

    rows[row_of_interest] = compact(rows[row_of_interest])
    row_blocked = sum([1 for c in blocked_coords if c.y == row_of_interest])

    return sum([x1 - x0 for x0, x1 in rows[row_of_interest]]) - row_blocked


if __name__ == "__main__":
    import unittest

    X = 26
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/15/test_input"), X)

    print(f"The result is {part1()}")
