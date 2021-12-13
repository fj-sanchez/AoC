import itertools


def part1(input_filepath="input"):
    with open(input_filepath) as f:
        lines = f.readlines()

    dots = {
        tuple(map(int, dot.strip().split(",")))
        for dot in itertools.takewhile(lambda x: x.strip(), lines)
    }
    folds = []
    for fold in lines[len(dots) + 1 :]:
        fold_type, fold_pos = fold.strip().split("=")
        folds.append((fold_type[-1], int(fold_pos)))

    for fold in folds[:1]:
        fold_type, fold_pos = fold
        new_dots = set()
        if fold_type == "x":
            for (dot_x, dot_y) in dots:
                if dot_x >= fold_pos:
                    new_dot_x = 2 * fold_pos - dot_x
                    new_dots.add((new_dot_x, dot_y))
                else:
                    new_dots.add((dot_x, dot_y))
        if fold_type == "y":
            for (dot_x, dot_y) in dots:
                if dot_y >= fold_pos:
                    new_dot_y = 2 * fold_pos - dot_y
                    new_dots.add((dot_x, new_dot_y))
                else:
                    new_dots.add((dot_x, dot_y))

    return len(new_dots)


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part1("test_input"), 17)

    print(f"The result is {part1()}")
