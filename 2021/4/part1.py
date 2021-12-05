from typing import List, Set


class Board:
    def __init__(self, board_lines: List[str]) -> None:
        self.rows = [[int(n) for n in line.split()] for line in board_lines]
        self.cols = [[self.rows[row][col] for row in range(5)] for col in range(5)]

    def check_board(self, numbers: Set[int]) -> int:
        winner = False
        score = 0
        for row in self.rows:
            unchecked_numbers = set(row) - numbers
            if not unchecked_numbers:
                winner = True
            score += sum(unchecked_numbers)
        if not winner:
            for col in self.cols:
                unchecked_numbers = set(col) - numbers
                if not unchecked_numbers:
                    winner = True

        return score if winner else 0


def part1(input_filepath="input"):
    with open(input_filepath) as f:
        lines = f.readlines()
    numbers = [int(n) for n in lines.pop(0).split(",")]
    boards = []
    for board_ix in range(len(lines) // 6):
        board_start_line = board_ix * 6 + 1
        board_lines = lines[board_start_line : board_start_line + 5]
        boards.append(Board(board_lines))

    extracted_numbers = set()
    for number in numbers:
        extracted_numbers.add(number)
        for board in boards:
            score = board.check_board(extracted_numbers)
            if score > 0:
                return score * number
    return 0


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part1("test_input"), 4512)

    print(f"The result is {part1()}")
