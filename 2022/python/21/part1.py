def part1(input_filepath="../../data/21/input"):
    with open(input_filepath) as f:
        monkeys = {monkey.replace(":", "=") for monkey in f.read().splitlines()}

    result = None
    completed = False
    while not completed:
        completed = True
        for monkey in monkeys.copy():
            try:
                exec(monkey)
                monkeys.remove(monkey)
            except NameError:
                completed = False
    return int(locals()["root"])


if __name__ == "__main__":
    import unittest

    X = 152
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/21/test_input"), X)

    print(f"The result is {part1()}")
