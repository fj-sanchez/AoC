from collections import deque
from operator import add, mul
from functools import partial
from typing import Deque, Iterable, Callable, Tuple, List, Dict

Item = int

_monkeys: Dict[str, "Monkey"] = {}


class Monkey:
    def __init__(
        self,
        monkey_id: str,
        starting_items: Iterable[int],
        operation: Callable[[int], int],
        test: int,
        next_if_true: str,
        next_if_false: str,
    ):
        self._id = monkey_id
        self._items: Deque[Item] = deque()
        self._operation: Callable[[int], int] = operation
        self._test: int = test
        self._next_if_true: str = next_if_true
        self._next_if_false: str = next_if_false
        self.inspected_items: int = 0

        for item in starting_items:
            self._items.append(item)

        # add self to monkey
        _monkeys[self._id] = self

    # def new_item(self, item) -> Item:
    #     return self._operation(item)
    #
    # def test(self, item: Item) -> bool:
    #     return (item % self._test) == 0
    #
    # def catch_item(self, item) -> None:
    #     self._items.append(item)
    #
    # def send_to_next_monkey(self, item: Item) -> None:
    #     next_monkey_id = self._next_if_true if self.test(item) else self._next_if_false
    #     next_monkey = _monkeys[next_monkey_id]
    #     next_monkey.catch_item(item)

    def do_turn(self) -> None:
        while self._items:
            item: Item = self._items.popleft()
            new_item = self._operation(item) // 3
            next_monkey_id = (
                self._next_if_true
                if (new_item % self._test) == 0
                else self._next_if_false
            )
            next_monkey = _monkeys[next_monkey_id]
            next_monkey._items.append(new_item)
            self.inspected_items += 1


class StressfulMonkey(Monkey):
    def __init__(
        self,
        monkey_id: str,
        starting_items: Iterable[int],
        operation: Callable[[int], int],
        test: int,
        next_if_true: str,
        next_if_false: str,
    ):
        super().__init__(
            monkey_id, starting_items, operation, test, next_if_true, next_if_false
        )
        self._mod = 1

    def set_mod(self, mod_):
        self._mod = mod_

    def do_turn(self) -> None:
        while self._items:
            item: Item = self._items.popleft()
            new_item = self._operation(item % self._mod)
            next_monkey_id = (
                self._next_if_true
                if (new_item % self._test) == 0
                else self._next_if_false
            )
            next_monkey = _monkeys[next_monkey_id]
            next_monkey._items.append(new_item)
            self.inspected_items += 1


def monkey_factory(
    monkey_definition: List[str], monkey_class=Monkey
) -> Tuple[str, Monkey, int]:
    if len(monkey_definition) != 6:
        raise ValueError(
            f"A Monkey is defined exactly by 6 lines, received {len(monkey_definition)}"
        )

    monkey_id = monkey_definition[0][7]
    starting_items = [
        int(item.strip()) for item in monkey_definition[1][18:].split(",")
    ]
    operator = mul if monkey_definition[2][23] == "*" else add
    operand = monkey_definition[2][25:]
    test = int(monkey_definition[3][21:])

    if operand == "old":
        operation = partial(lambda item_: operator(item_, item_))
    else:
        operation = partial(lambda item_: operator(item_, int(operand)))

    next_monkey_if_true = monkey_definition[4][29:]
    next_monkey_if_false = monkey_definition[5][30:]

    return (
        monkey_id,
        monkey_class(
            monkey_id,
            starting_items,
            operation,
            test,
            next_monkey_if_true,
            next_monkey_if_false,
        ),
        test,
    )
