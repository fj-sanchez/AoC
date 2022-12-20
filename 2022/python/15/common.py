import re
from collections import namedtuple
from typing import List

XY = namedtuple("XY", ["x", "y"])
XSPAN = namedtuple("XSPAN", ["x0", "x1"])
Sensor = namedtuple("Sensor", ["x", "y", "beacon_x", "beacon_y"])


def parse_input(lines: List[str]) -> List[Sensor]:
    parse_regex = re.compile(
        r"x=(?P<x>-?\d+), y=(?P<y>-?\d+).*x=(?P<beacon_x>-?\d+), y=(?P<beacon_y>-?\d+)"
    )

    sensors: List[Sensor] = []
    for line in lines:
        match = parse_regex.search(line)
        sensors.append(Sensor(**{k: int(v) for k, v in match.groupdict().items()}))

    return sensors


def compact(rows: List[XSPAN]) -> List[XSPAN]:
    if len(rows) < 2:
        return rows
    rows_ = sorted(rows)
    spans = list()
    tmp = rows_[0]
    for r in rows_[1:]:
        if tmp.x1 >= r.x0:
            tmp = XSPAN(tmp.x0, max(tmp.x1, r.x1))
        else:
            spans.append(tmp)
            tmp = r
    spans.append(tmp)
    return spans
