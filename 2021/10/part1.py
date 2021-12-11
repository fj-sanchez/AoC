import collections

collections

opening = "({[<"
closing = ")}]>"
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}


def part1(input_filepath="input"):
    with open(input_filepath) as f:
        data = f.readlines()

    q = collections.deque()
    score = 0
    for line in data:
        q.clear()
        for c in line.strip():
            if c in opening:
                q.append(c)
            else:
                prev = q.pop()
                if prev not in opening or opening.index(prev) != closing.index(c):
                    score += scores[c]

    return score


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part1("test_input"), 26397)

    print(f"The result is {part1()}")
