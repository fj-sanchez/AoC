import collections
import operator
import itertools


def sum_window(iterable, n):
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield sum(window)
    for x in it:
        window.append(x)
        yield sum(window)


def part1(input_filepath="input"):
    with open(input_filepath) as f:
        data = list(map(int, f.readlines()))

    result = sum(map(operator.lt, sum_window(data, 3), sum_window(data[1:], 3)))

    return result


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part1("test_input"), 5)

    print(f"The result is {part1()}")
