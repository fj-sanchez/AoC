from collections import defaultdict
from typing import List, Dict, Set
from common import parse_input, compact, XSPAN, XY

LIMITS = iter([(0, 20), (0, 4000000)])


def part2(input_filepath="../../data/15/input"):
    with open(input_filepath) as f:
        data = f.readlines()

    min_limit, max_limit = next(LIMITS)

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
        for dy in range(0, dist + 1):
            dx = dist - dy
            if dx == 0 and dy == 0:
                raise ValueError("Unexpected")
            if min_limit <= sensor.y + dy < max_limit + 1:
                rows[sensor.y + dy].append(XSPAN(sensor.x - dx, sensor.x + dx + 1))
                rows[sensor.y + dy] = compact(rows[sensor.y + dy])
            if dy > 0 and min_limit <= sensor.y - dy < max_limit + 1:
                rows[sensor.y - dy].append(XSPAN(sensor.x - dx, sensor.x + dx + 1))
                rows[sensor.y - dy] = compact(rows[sensor.y - dy])

    for r, spans in rows.items():
        if min_limit <= r < max_limit + 1:
            spans = compact(spans)
            if len(spans) > 1:
                for span in spans[:-1]:
                    if min_limit <= span.x1 < max_limit + 1:
                        return span.x1 * 4000000 + r

    return 0


if __name__ == "__main__":
    import unittest

    X = 56000011
    tc = unittest.TestCase()
    tc.assertEqual(part2("../../data/15/test_input"), X)

    print(f"The result is {part2()}")
