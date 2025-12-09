def is_invalid_id(n: int) -> bool:
    s = str(n)
    # Check if s is built from repeating a smaller substring ≥ 2 times
    return s in (s + s)[1:-1]


def sum_invalid_ids(input_line: str) -> int:
    total = 0
    ranges = input_line.strip().split(',')

    for r in ranges:
        if not r:
            continue
        lo, hi = map(int, r.split('-'))

        for num in range(lo, hi + 1):
            if is_invalid_id(num):
                total += num

    return total


# ---- Usage ----
input_line = input().strip()
print(sum_invalid_ids(input_line))
