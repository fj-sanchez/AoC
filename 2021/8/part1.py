import dataclasses
from typing import List


@dataclasses.dataclass
class Entry:
    samples: List[str]
    outputs: List[str]

    def count_unique_patterns(self):
        LEN_OF_DIGITS_WITH_UNIQUE_PATTERN = (2, 3, 4, 7)
        return sum(1 for output in self.outputs if len(output) in LEN_OF_DIGITS_WITH_UNIQUE_PATTERN)


def part1(input_filepath="input"):
    with open(input_filepath) as f:
        entries = [
            Entry(samples.split(), outputs.split())
            for samples, outputs in [tuple(line.split("|")) for line in f.readlines()]
        ]

    count_unique = sum(entry.count_unique_patterns() for entry in entries)

    return count_unique


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part1("test_input"), 26)

    print(f"The result is {part1()}")
