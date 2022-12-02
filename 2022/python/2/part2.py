def part2(input_filepath="../../data/2/input"):
    with open(input_filepath) as f:
        data = f.readlines()

    # rock, paper, scissor
    moves = {"A": 1, "B": 2, "C": 3}
    outcome_to_move_inc = {"X": 2, "Y": 0, "Z": 1}
    outcome = {"X": 0, "Y": 3, "Z": 6}

    def score(p1, p2) -> int:
        outcome_score = outcome[p2]
        played_move = ((moves[p1] - 1 + outcome_to_move_inc[p2]) % 3) + 1
        match_score = outcome_score + played_move
        return match_score

    total_score = 0
    for match in data:
        total_score += score(*match.split())

    return total_score


if __name__ == "__main__":
    import unittest

    X = 12
    tc = unittest.TestCase()
    tc.assertEqual(part2("../../data/2/test_input"), X)

    print(f"The result is {part2()}")
