


def get_largest_value(input_string: str) -> int : 
    largest_tens = 1
    largest_ones = 1
    idx = 0
    size = len(input_string)
    for i in range(0, size -  1) : 
        if(int(input_string[i]) > largest_tens and i < size - 1 ):
            largest_tens = int(input_string[i])
            idx = i

    for j  in range(idx  + 1,  size ) :
        if(int(input_string[j]) > largest_ones):
            largest_ones = int(input_string[j])

    return largest_tens * 10 + largest_ones


def get_largest_value_different(s: str) -> int:
    n = len(s)
    if n < 2:
        return 0
    # max_from_right[i] = max digit in s[i:]
    max_from_right = [0] * n
    cur = -1
    for i in range(n - 1, -1, -1):
        d = int(s[i])
        if d > cur:
            cur = d
        max_from_right[i] = cur

    best = 0
    for i in range(n - 1):          # i can be tens digit, must have j > i
        tens = int(s[i])
        ones = max_from_right[i + 1]
        best = max(best, tens * 10 + ones)

    return best

if __name__ == "__main__" :
    import sys
    total = 0 
    total_different = 0
    count = 0
    for line in sys.stdin :
        line = line.rstrip("\n")
        count += 1
        if not line:
            continue
        total += get_largest_value(line)    
        # total_different += get_largest_value_different(line)
        # x = get_largest_value_different(line)
        y = get_largest_value(line)
        # print(f"{x} {y} diff = {x - y} \t idx = {count}") if (x != y) else None 

    print(total)
    print(total_different)


    









