def part1(input_filepath="../../data/6/input"):
    with open(input_filepath) as f:
        data = f.read()

    MARKER_LEN = 4
    total_len = len(data)
    ix = MARKER_LEN
    found = False
    while ix <= total_len and not found:
        if len(set(data[ix - MARKER_LEN : ix])) == MARKER_LEN:
            found = True
            continue
        ix += 1

    return ix


if __name__ == "__main__":
    import unittest

    X = 7
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/6/test_input"), X)

    print(f"The result is {part1()}")
