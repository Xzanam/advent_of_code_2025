def is_invalid_id(n: int) -> bool:
    """Check if a number is of the form X repeated twice."""
    s = str(n)
    length = len(s)
    
    # Must be even length to split into two equal halves
    if length % 2 != 0:
        return False
    
    half = length // 2
    return s[:half] == s[half:]


def sum_invalid_ids(input_line: str) -> int:
    total = 0
    ranges = input_line.strip().split(',')

    for r in ranges:
        if not r:
            continue  # ignore empty segments if trailing comma exists
        
        lo, hi = map(int, r.split('-'))
        
        for num in range(lo, hi + 1):
            if is_invalid_id(num):
                total += num

    return total


# ----------------------------
# Example usage:
# ----------------------------

if __name__ == "__main__":
    input_line = input().strip()
    print(sum_invalid_ids(input_line))
