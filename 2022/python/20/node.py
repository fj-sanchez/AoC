from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Node:
    value: int
    prev: Optional["Node"]
    next: Optional["Node"]

    def mix(self, max_len: int):
        if self.value == 0:
            # print("0 does not move:")
            return
        # if self.value > 0:
        insert_point = self
        for _ in range(self.value % (max_len - 1)):
            insert_point = insert_point.next
        # else:
        #     insert_point = self
        #     for _ in range((abs(self.value) + 1 % (max_len - 1)):
        #         insert_point = insert_point.prev

        # print(
        #     f"{self.value} moves between {insert_point.value} and {insert_point.next.value}:"
        # )

        if insert_point == self:
            return

        self.prev.next = self.next
        self.next.prev = self.prev

        self.prev = insert_point
        self.next = insert_point.next

        insert_point.next.prev = self
        insert_point.next = self


def print_nodes(nodes: List[Node], root: Node):
    v = []
    n = root
    for _ in range(min(7, len(nodes))):
        v.append(str(n.value))
        n = n.next
    print(", ".join(v) + "\n")


def create_nodes(data, node_cls):
    nodes = []
    zero = None
    for d in data:
        n = node_cls(d, None, None)
        if n.value == 0:
            zero = n
        if nodes:
            n.prev = nodes[-1]
            nodes[-1].next = n
        nodes.append(n)
    nodes[0].prev = nodes[-1]
    nodes[-1].next = nodes[0]
    return nodes, zero


@dataclass
class Node2(Node):
    DKEY = 811589153

    def __post_init__(self):
        self.value *= Node2.DKEY
