import collections

collections

opening = "({[<"
closing = ")}]>"
score_lookup = {"(": 1, "[": 2, "{": 3, "<": 4}


def part2(input_filepath="input"):
    with open(input_filepath) as f:
        data = f.readlines()

    q = collections.deque()
    line_scores = []
    for line in data:
        q.clear()
        for c in line.strip():
            if c in opening:
                q.append(c)
            else:
                prev = q.pop()
                if prev not in opening or opening.index(prev) != closing.index(c):
                    q.clear()
                    break
        if len(q):
            score = 0
            for c in reversed(q):
                score = score * 5 + score_lookup[c]
            line_scores.append(score)

    return sorted(line_scores)[len(line_scores) // 2]


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part2("test_input"), 288957)

    print(f"The result is {part2()}")
