import dataclasses
import heapq
import itertools
from typing import (
    Tuple,
    Any,
    List,
    Iterator,
    Dict,
    Optional,
    Callable,
    Generic,
    TypeVar,
    Union,
    Set,
    FrozenSet,
)

T = TypeVar("T")
Node = Tuple[int, T]
Position = Tuple[int, int]
Numeric = Union[int, float]


@dataclasses.dataclass(eq=True, frozen=True)
class GraphNode:
    position: Position
    g: Numeric = dataclasses.field(hash=False, compare=False)
    depth: Numeric = dataclasses.field(hash=False, compare=False)
    parent_node: Optional["GraphNode"] = dataclasses.field(hash=False, compare=False)
    f: Optional[Numeric] = dataclasses.field(default=0.0, hash=False, compare=False)


@dataclasses.dataclass(order=True, eq=True, unsafe_hash=True, frozen=False)
class QueueEntry:
    priority: int
    counter: int
    value: Any


class PriorityQueue(Generic[T]):
    """
    A queue structure where each element is served in order of priority.

    Elements in the queue are popped based on the priority with higher priority
    elements being served before lower priority elements.  If two elements have
    the same priority, they will be served in the order they were added to the
    queue.
    """

    DELETED = object()

    def __init__(self, enable_updates: bool = False):
        """Initialize a new Priority Queue."""

        self._enable_updates = enable_updates
        self._queue: List[QueueEntry] = []
        self._counter: Iterator[int] = itertools.count()
        self._entry_map: Dict[T, QueueEntry] = {}

    @property
    def queue(self) -> Iterator[Node]:
        return map(
            lambda entry: (entry.priority, entry.value),
            filter(lambda entry: entry.value != PriorityQueue.DELETED, self._queue),
        )

    def pop(self) -> Node:
        """
        Pop top priority node from queue.

        Returns:
            The node with the highest priority.
        """

        while self._queue:
            entry = heapq.heappop(self._queue)
            if entry.value is not PriorityQueue.DELETED:
                try:
                    del self._entry_map[entry.value]
                except KeyError:
                    if self._enable_updates:
                        raise
                return entry.priority, entry.value
        raise KeyError("Priority queue is empty.")

    def remove(self, node: Node):
        """
        Remove a node from the queue.

        Args:
            node (tuple): The node to remove from the queue.
        """
        assert self._enable_updates
        _, value = node
        entry = self._entry_map.pop(value)
        entry.value = PriorityQueue.DELETED

    def __iter__(self):
        """Queue iterator."""

        return self.queue

    def __str__(self):
        """Priority Queue to string."""

        return "PQ:%s" % self.queue

    def append(self, node: Node):
        """
        Append a node to the queue.

        Args:
            node: Comparable Object to be added to the priority queue.
        """
        priority, value = node
        entry = QueueEntry(priority, next(self._counter), value)

        if self._enable_updates:
            if value in self._entry_map:
                self.remove(node)
            self._entry_map[value] = entry

        heapq.heappush(self._queue, entry)

    def __contains__(self, key: T):
        """
        Containment Check operator for 'in'

        Args:
            key: The key to check for in the queue.

        Returns:
            True if key is found in queue, False otherwise.
        """
        if self._enable_updates:
            return key in self._entry_map

        return key in [n[-1] for n in self.queue]

    def __eq__(self, other):
        """
        Compare this Priority Queue with another Priority Queue.

        Args:
            other (PriorityQueue): Priority Queue to compare against.

        Returns:
            True if the two priority queues are equivalent.
        """

        return all(val == val_other for val, val_other in zip(self.queue, other.queue))

    def size(self):
        """
        Get the current size of the queue.

        Returns:
            Integer of number of items in queue.
        """
        if self._enable_updates:
            return len(self._entry_map)
        return len(self._queue)

    def clear(self):
        """Reset queue to empty (no nodes)."""

        self._queue = []
        self._entry_map = {}

    def top(self):
        """
        Get the top item in the queue.

        Returns:
            The first item stored in the queue.
        """

        return next(self.queue)

    def get(self, value: Any) -> Node:
        """
        Get a specific item from the Priority Queue by value.

        Args:
            value (Any): value of the Node to return.

        Returns:
            The Node in the queue.
        """
        entry = None
        if self._enable_updates:
            entry = self._entry_map[value]
        else:
            for queued_entry in self._queue:
                if queued_entry.value == value:
                    entry = queued_entry
        if entry is None:
            raise IndexError(f"The node {value} cannot be found in the queue.")
        return entry.priority, entry.value


def expand_node(
    map_,
    node: GraphNode,
    explored: Dict[Position, GraphNode],
    fringe: PriorityQueue[GraphNode],
) -> List[GraphNode]:
    successors = []

    max_i, max_j = len(map_), len(map_[0])
    i, j = node.position

    for (di, dj) in itertools.product([-1, 0, 1], [-1, 0, 1]):
        if di == dj == 0 or (abs(di) + abs(dj)) == 2:
            continue
        a_i, a_j = i + di, j + dj
        if 0 <= a_i < max_i and 0 <= a_j < max_j:
            neighbour = a_i, a_j
        else:
            continue

        successor = GraphNode(
            position=neighbour,
            g=node.g + map_[a_i][a_j],
            depth=node.depth + 1,
            parent_node=node,
        )

        if successor.position in explored:
            explored_node = explored[successor.position]
            if explored_node.g > successor.g:
                explored[successor.position] = successor
        elif successor in fringe:
            in_fringe_priority_node, in_fringe_node = fringe.get(successor)
            if in_fringe_node.g > successor.g:
                fringe.remove((in_fringe_priority_node, in_fringe_node))
                successors.append(successor)
        else:
            successors.append(successor)

    return successors


def search_ucs(map_):
    max_i = len(map_)
    max_j = len(map_[0])

    frontier: PriorityQueue[GraphNode] = PriorityQueue(enable_updates=True)
    start = (0, 0)
    start_node = GraphNode(position=start, g=0, depth=0, parent_node=None)
    goal = (max_i - 1, max_j - 1)
    goal_node = None
    frontier.append((start_node.g, start_node))
    explored = {}

    while frontier.size() > 0:
        _, node = frontier.pop()
        if goal_node is None or node.g < goal_node.g:
            successors = expand_node(
                map_,
                node,
                explored,
                frontier,
            )
        else:
            break
        explored[node.position] = node
        for successor in successors:
            if successor.position == goal:
                goal_node = successor
            frontier.append((successor.g, successor))

    if goal_node is None:
        raise ValueError(f"Couldn't find a path from {start} to {goal}.")
    return goal_node.g


def part1(input_filepath="input"):
    with open(input_filepath) as f:
        map_ = list(map(lambda l: list(map(int, l.strip())), f.readlines()))
    result = search_ucs(map_)

    return result


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part1("test_input"), 40)

    print(f"The result is {part1()}")
