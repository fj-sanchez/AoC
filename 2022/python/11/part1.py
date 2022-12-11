from typing import Dict

from monkey import monkey_factory, Monkey


ROUNDS = 20


def part1(input_filepath="../../data/11/input"):
    with open(input_filepath) as f:
        data = f.read()
    data = list(filter(lambda x: x, data.splitlines()))

    monkeys: Dict[str, Monkey] = {}
    group = lambda t, n: zip(*[t[i::n] for i in range(n)])
    for monkey_definition in group(data, 6):
        monkey_id, monkey, _ = monkey_factory(monkey_definition)
        monkeys[monkey_id] = monkey

    for _ in range(ROUNDS):
        for monkey in monkeys.values():
            monkey.do_turn()

    inspected = [monkey.inspected_items for monkey in monkeys.values()]
    m1, m2 = sorted(inspected, reverse=True)[:2]
    return m1 * m2


if __name__ == "__main__":
    import unittest

    X = 10605
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/11/test_input"), X)

    print(f"The result is {part1()}")
