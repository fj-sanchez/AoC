from node import Node2, create_nodes, print_nodes


def part2(input_filepath="../../data/20/input"):
    with open(input_filepath) as f:
        data = map(int, f.readlines())

    nodes, zero = create_nodes(data, Node2)

    # print("Initial arrangement:")
    # print_nodes(nodes, zero)
    num_nodes = len(nodes)
    for i in range(1, 11):
        # print(f"After {i} rounds of mixing")
        # print_nodes(nodes, zero)
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

    X = 1623178306
    tc = unittest.TestCase()
    tc.assertEqual(part2("../../data/20/test_input"), X)

    print(f"The result is {part2()}")
