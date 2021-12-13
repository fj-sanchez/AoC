import copy
import dataclasses
from typing import List, Dict, Deque, Optional, Set
import collections


@dataclasses.dataclass(frozen=False)
class Cave:
    name: str
    links: List["Cave"] = dataclasses.field(compare=False)

    def is_big(self) -> bool:
        return self.name == self.name.upper()

    def add_link(self, cave: "Cave"):
        if cave not in self.links:
            self.links.append(cave)


@dataclasses.dataclass
class Node:
    name: str
    path: List[str]


def dfs_all_paths(caves: Dict[str, Cave]) -> List[List[str]]:
    frontier: Deque[Node] = collections.deque()
    paths: List[List[str]] = []

    frontier.append(Node("start", list(("start",))))
    while len(frontier) > 0:
        node = frontier.pop()
        if node.name == "end":
            paths.append(node.path)
            continue

        for link in filter(
            lambda c: c.is_big() or c.name not in node.path, caves[node.name].links
        ):
            n = Node(name=link.name, path=copy.copy(node.path))
            n.path.append(link.name)
            frontier.append(n)

    return paths


def part1(input_filepath="input"):
    with open(input_filepath) as f:
        links = [line.strip().split("-") for line in f.readlines()]

    caves: Dict[str, Cave] = {}
    for (cave_a, cave_b) in links:
        for cave in [cave_a, cave_b]:
            if cave not in caves:
                caves[cave] = Cave(cave, list())
        caves[cave_a].add_link(caves[cave_b])
        caves[cave_b].add_link(caves[cave_a])

    all_paths = dfs_all_paths(caves)

    return len(all_paths)


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part1("sample"), 10)
    tc.assertEqual(part1("test_input"), 19)
    tc.assertEqual(part1("test_input2"), 226)

    print(f"The result is {part1()}")
