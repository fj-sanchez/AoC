def part1(input_filepath="../../data/2/input"):
    with open(input_filepath) as f:
        data = f.readlines()

    # rock, paper, scissor
    move_to_score = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

    def score(p1, p2) -> int:
        match_score = 0
        diff = move_to_score[p1] - move_to_score[p2]
        if diff in (-2, 1):
            match_score = move_to_score[p2]
        if diff == 0:
            match_score = move_to_score[p2] + 3
        elif diff in (-1, 2):
            match_score = move_to_score[p2] + 6
        return match_score

    total_score = 0
    for match in data:
        total_score += score(*match.split())

    return total_score


if __name__ == "__main__":
    import unittest

    X = 15
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/2/test_input"), X)

    print(f"The result is {part1()}")
