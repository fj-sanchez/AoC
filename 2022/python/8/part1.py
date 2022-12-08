from itertools import product


def part1(input_filepath="../../data/8/input"):
    with open(input_filepath) as f:
        rows = list(map(list, f.read().splitlines()))

    num_rows = len(rows)
    num_cols = len(rows[0])
    cols = [[rows[row][col] for row in range(num_rows)] for col in range(num_cols)]

    # add side trees coordinates to visible trees
    visible_trees = {(i, j) for i, j in product(range(num_cols), (0, num_rows - 1))}
    visible_trees.update({(i, j) for i, j in product((0, num_cols - 1), range(num_rows))})

    # get visible trees horizontally
    for j, row in enumerate(rows[1:-1]):
        rank = row[0]
        for i in range(1, len(row) - 1):
            if row[i] > rank:
                visible_trees.add((i, j + 1))
                rank = row[i]
        rank = row[-1]
        for i in range(len(row) - 2, 0, -1):
            if row[i] > rank:
                visible_trees.add((i, j + 1))
                rank = row[i]

    # get visible trees vertically
    for i, col in enumerate(cols[1:-1]):
        rank = col[0]
        for j in range(1, len(col) - 1):
            if col[j] > rank:
                visible_trees.add((i + 1, j))
                rank = col[j]
        rank = col[-1]
        for j in range(len(col) - 1, 0, -1):
            if col[j] > rank:
                visible_trees.add((i + 1, j))
                rank = col[j]

    return len(visible_trees)


if __name__ == "__main__":
    import unittest

    X = 21
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/8/test_input"), X)

    print(f"The result is {part1()}")
