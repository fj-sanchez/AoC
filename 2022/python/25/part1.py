from math import log, ceil

PLUS_ONE = {"=": "-", "-": "0", "0": "1", "1": "2", "2": "="}


def add_one(code: str) -> str:
    new_code = ""
    i = len(code) - 1
    carry = True
    while carry:
        c = code[i]
        new_code += PLUS_ONE[c]
        carry = True if c == "2" else False
        i -= 1

    code = code[: i + 1] + "".join(reversed(new_code))
    return code


def part1(input_filepath="../../data/25/input"):
    with open(input_filepath) as f:
        data = f.read().splitlines()

    total = 0
    for l in data:
        total += sum([5**i * int(n.replace("-", "-1").replace("=", "-2"), 5) for i, n in enumerate(reversed(l))])

    code = ""
    max_digits = ceil(log(total) / log(5))
    while max_digits >= 0:
        q = total // (5**max_digits)
        r = total % (5**max_digits)

        if q == 4:
            code = add_one(code)
            code += "-"
        elif q == 3:
            code = add_one(code)
            code += "="
        else:
            code += str(q)
        total = r
        max_digits -= 1
    code = code.lstrip("0")

    return code


if __name__ == "__main__":
    import unittest

    X = "2=-1=0"
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/25/test_input"), X)

    print(f"The result is {part1()}")
