def scenic_score_1d(tree_line):
    if not tree_line:
        return 0
    rank = tree_line[0]
    score = 0
    for tree in tree_line[1:]:
        score += 1
        if tree >= rank:
            break
    return score


def part2(input_filepath="../../data/8/input"):
    with open(input_filepath) as f:
        rows = list(map(list, f.read().splitlines()))

    num_rows = len(rows)
    num_cols = len(rows[0])
    cols = [[rows[row][col] for row in range(num_rows)] for col in range(num_cols)]

    scores = [[0 for _ in range(num_rows)] for _ in range(num_cols)]
    # get scenic tree score horizontally
    for i, row in enumerate(rows):
        for j in range(num_cols):
            scores[i][j] = scenic_score_1d(row[j:]) * scenic_score_1d(
                list(reversed(row[: j + 1]))
            )
    # get scenic tree score vertically
    for j, col in enumerate(cols):
        for i in range(num_rows):
            scores[i][j] *= scenic_score_1d(col[i:]) * scenic_score_1d(
                list(reversed(col[: i + 1]))
            )

    return max([max(row) for row in scores])


if __name__ == "__main__":
    import unittest

    X = 8
    tc = unittest.TestCase()
    tc.assertEqual(part2("../../data/8/test_input"), X)

    print(f"The result is {part2()}")
