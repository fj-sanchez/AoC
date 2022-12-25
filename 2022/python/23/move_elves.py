ALL_DIRS = {(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)}
DIRS = {
    (0, 1): {(-1, 1), (0, 1), (1, 1)},
    (0, -1): {(-1, -1), (0, -1), (1, -1)},
    (-1, 0): {(-1, -1), (-1, 0), (-1, 1)},
    (1, 0): {(1, -1), (1, 0), (1, 1)},
}


def parse_input(input_filepath):
    with open(input_filepath) as f:
        data = [list(l) for l in f.read().splitlines()]
    elves = {(x, -y) for y, row in enumerate(data) for x, v in enumerate(row) if v == "#"}
    return elves


def print_grid(elves):
    x = [e[0] for e in sorted(elves)]
    y = [e[1] for e in sorted(elves)]
    min_x = min(x)
    min_y = min(y)
    p = [["." for _ in range(min_x, max(x) + 1)] for _ in range(min_y, max(y) + 1)]

    for x, y in elves:
        p[y - min_y][x - min_x] = "#"
    for r in reversed(p):
        print("".join(r))
    print("\n\n")


def move_elves(elves, dirs):
    updated = False
    proposed = {}
    for elf in sorted(elves):
        if all([(elf[0] + check[0], elf[1] + check[1]) not in elves for check in ALL_DIRS]):
            continue
        else:
            updated = True
        for move, checks in dirs.items():
            if all([(elf[0] + check[0], elf[1] + check[1]) not in elves for check in checks]):
                proposed.setdefault((elf[0] + move[0], elf[1] + move[1]), set()).add(elf)
                break
    for p, e in proposed.items():
        if len(e) == 1:
            elves.remove(e.pop())
            elves.add(p)

    return updated


def rotate_dirs(dirs):
    k = list(dirs.keys())[0]
    v = dirs.pop(k)
    dirs[k] = v
