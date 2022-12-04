def part1(input_filepath="../../data/4/input"):
    with open(input_filepath) as f:
        data = f.read().splitlines()

    def get_sections(l):
        for i in l:
            s1, s2 = i.split(",")
            s1 = s1.split("-")
            s1 = set(range(int(s1[0]), int(s1[1]) + 1))
            s2 = s2.split("-")
            s2 = set(range(int(s2[0]), int(s2[1]) + 1))
            yield s1, s2

    total = 0
    for sec1, sec2 in get_sections(data):
        if sec1.issubset(sec2) or sec2.issubset(sec1):
            total += 1

    return total


if __name__ == "__main__":
    import unittest

    X = 2
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/4/test_input"), X)

    print(f"The result is {part1()}")
