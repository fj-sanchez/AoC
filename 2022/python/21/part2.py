from collections import namedtuple
from operator import sub, add, mul, truediv
from typing import Set, Dict

MonkeyOp = namedtuple("MonkeyOp", ["left", "op", "right"])


def part2(input_filepath="../../data/21/input"):
    with open(input_filepath) as f:
        monkeys: Set[str] = {
            monkey.replace(":", "=") for monkey in f.read().splitlines()
        }

    root = None
    me = None
    done = 0
    for monkey in monkeys.copy():
        if monkey.startswith("root="):
            root = monkey
            monkeys.remove(root)
            done += 1
        elif monkey.startswith("humn="):
            me = monkey
            monkeys.remove(me)
            done += 1
        if done >= 2:
            break

    completed = False
    updated = True
    while not completed and updated:
        completed = True
        updated = False
        for monkey in monkeys.copy():
            try:
                exec(monkey)
                monkeys.remove(monkey)
                updated = True
            except NameError:
                completed = False

    root_left, root_right = tuple(root[6:].replace(" ", "").split("+"))
    if root_left in locals():
        sol = eval(root_left)
        unknown = root_right
    elif root_right in locals():
        sol = eval(root_right)
        unknown = root_left
    else:
        raise ValueError("Hell...")

    monkey_ops: Dict[str, MonkeyOp] = {}
    a = {}
    for monkey in monkeys:
        monkey_ops[monkey[0:4]] = MonkeyOp(monkey[6:10], monkey[11], monkey[13:17])

    op_to_inverse_op = {"+": sub, "-": add, "/": mul, "*": truediv}

    while unknown != "humn":
        monkey_op = monkey_ops[unknown]
        if monkey_op.left in locals():
            known_operand = eval(monkey_op.left)
            unknown = monkey_op.right
        else:
            known_operand = eval(monkey_op.right)
            unknown = monkey_op.left
        # the below case doesn't exist in the input
        # if monkey_op.op == "/" and unknown == monkey_op.right:
        #     sol = 1/sol
        if monkey_op.op == "-" and unknown == monkey_op.right:
            sol = -sol
        sol = op_to_inverse_op[monkey_op.op](sol, known_operand)

    return sol


if __name__ == "__main__":
    import unittest

    X = 301
    tc = unittest.TestCase()
    tc.assertEqual(part2("../../data/21/test_input"), X)

    print(f"The result is {part2()}")
