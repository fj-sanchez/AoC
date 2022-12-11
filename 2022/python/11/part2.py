from typing import Dict

from monkey import monkey_factory, StressfulMonkey

ROUNDS = 10000


def part2(input_filepath="../../data/11/input"):
    with open(input_filepath) as f:
        data = f.read()
    data = list(filter(lambda x: x, data.splitlines()))

    monkeys: Dict[str, StressfulMonkey] = {}
    group = lambda t, n: zip(*[t[i::n] for i in range(n)])
    modulus = 1
    for monkey_definition in group(data, 6):
        monkey_id, monkey, mod_ = monkey_factory(monkey_definition, StressfulMonkey)
        modulus *= mod_
        monkeys[monkey_id] = monkey

    for monkey in monkeys.values():
        monkey.set_mod(modulus)

    for r in range(1, ROUNDS + 1):
        for monkey in monkeys.values():
            monkey.do_turn()
        if r in (1, 20) or r % 1000 == 0:
            print(f"== After round {r} ==")
            for monkey in monkeys.values():
                print(
                    f"Monkey {monkey._id} inspected items {monkey.inspected_items} times"
                )
            print("\n")

    inspected = [monkey.inspected_items for monkey in monkeys.values()]
    m1, m2 = sorted(inspected, reverse=True)[:2]
    return m1 * m2


if __name__ == "__main__":
    import unittest

    X = 2713310158
    tc = unittest.TestCase()
    tc.assertEqual(part2("../../data/11/test_input"), X)
    print("Finished test")

    print(f"The result is {part2()}")
