from typing import List


class Entry:
    UNIQUE_LENGTHS = (2, 3, 4, 7)

    def __init__(self, samples: List[str], outputs: List[str]):
        self.samples = ["".join(sorted(list(s))) for s in samples]
        self.outputs = ["".join(sorted(list(o))) for o in outputs]

    def count_unique_patterns(self):
        return sum(1 for output in self.outputs if len(output) in Entry.UNIQUE_LENGTHS)

    def decode(self):
        mapping = {
            1: next(filter(lambda x: len(x) == 2, self.samples)),
            4: next(filter(lambda x: len(x) == 4, self.samples)),
            7: next(filter(lambda x: len(x) == 3, self.samples)),
            8: next(filter(lambda x: len(x) == 7, self.samples)),
        }
        decoder = {v: k for k, v in mapping.items()}
        mapping = {k: set(list(v)) for k, v in mapping.items()}
        for entry_str in filter(
            lambda x: len(x) not in Entry.UNIQUE_LENGTHS, sorted(self.samples, key=len)
        ):
            length = len(entry_str)
            entry = set(entry_str)
            if length == 5:
                if len((mapping[8] - mapping[4]) - entry) == 0:
                    mapping[2] = entry
                    decoder[entry_str] = 2
                elif len(mapping[7] - entry) == 0:
                    mapping[3] = entry
                    decoder[entry_str] = 3
                else:
                    mapping[5] = entry
                    decoder[entry_str] = 5
            elif length == 6:
                if len((mapping[4] - mapping[1]) - entry) == 1:
                    mapping[0] = entry
                    decoder[entry_str] = 0
                elif len(mapping[4] - entry) == 0:
                    mapping[9] = entry
                    decoder[entry_str] = 9
                else:
                    mapping[6] = entry
                    decoder[entry_str] = 6
        result = sum(
            decoder[output] * pow(10, pos)
            for pos, output in enumerate(reversed(self.outputs))
        )
        return result


def part2(input_filepath="input"):
    with open(input_filepath) as f:
        entries = [
            Entry(samples.split(), outputs.split())
            for samples, outputs in [tuple(line.split("|")) for line in f.readlines()]
        ]

    outputs = sum(list(map(lambda x: x.decode(), entries)))

    return outputs


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part2("test_input"), 61229)

    print(f"The result is {part2()}")
