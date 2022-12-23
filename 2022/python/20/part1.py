from node import Node, create_nodes


def part1(input_filepath="../../data/20/input"):
    with open(input_filepath) as f:
        data = map(int, f.readlines())

    nodes, zero = create_nodes(data, Node)

    # print("Initial arrangement:")
    # print_nodes(nodes, root)
    num_nodes = len(nodes)
    for node in nodes:
        node.mix(num_nodes)

    tmp = zero
    values = []
    reduced_interval = 1000 % len(nodes)
    for i in range(1, reduced_interval * 3 + 1):
        tmp = tmp.next
        if i % reduced_interval == 0:
            values.append(tmp.value)

    return sum(values)


if __name__ == "__main__":
    import unittest

    X = 3
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/20/test_input"), X)

    print(f"The result is {part1()}")
