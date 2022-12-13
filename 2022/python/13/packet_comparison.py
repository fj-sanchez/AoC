from itertools import zip_longest


class StopProcessingPacket(StopIteration):
    pass


def elements_in_order(left, right, pad=0):
    if left is not None and right is not None:
        print(f"{' '*pad}- Compare {left} vs {right}")
    pad += 1

    if left is None:
        print(
            f"{' '*pad}- Left side ran out of items, so inputs are in the right order"
        )
        raise StopProcessingPacket
    elif right is None:
        print(
            f"{' '*pad}- Right side will ran out of items, so inputs are not in the right order"
        )
        return False

    if type(left) != type(right):
        if isinstance(left, int):
            print(
                f"{' '*pad}- Mixed types; convert left to [{left}] and retry comparison"
            )
            left = [left]
        else:
            print(
                f"{' ' * pad}- Mixed types; convert right to [{right}] and retry comparison"
            )
            right = [right]
        return elements_in_order(left, right, pad)

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            print(f"{' '*pad}- Left side is smaller, so inputs are in the right order")
            raise StopProcessingPacket
        elif left > right:
            print(
                f"{' '*pad}- Right side is smaller, so inputs are not in the right order"
            )
        return left <= right

    result = []
    for l_val, r_val in zip_longest(left, right):
        result.append(elements_in_order(l_val, r_val, pad))
        if not result[-1]:
            break
    return all(result)


def compare_packets(left, right) -> int:
    try:
        x = 0 if elements_in_order(left, right) else 1
    except StopProcessingPacket:
        x = -1
    return x
