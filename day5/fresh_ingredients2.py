

import sys
if __name__ == "__main__" :

    ranges = []
    ingredients = []


    for line in sys.stdin : 
        line = line.rstrip("\n")

        if not line:
            break

        ranges.append( tuple( map(int, line.split('-'))))


    ranges.sort()
    merged_ranges = [] 

    for start, end in  ranges:
        if not merged_ranges or  start > merged_ranges[-1][1] + 1:
            merged_ranges.append( [start, end] )
        else: 
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)
    
    valid_count = 0
    for range_pair in merged_ranges:
        valid_count += ( range_pair[1] - range_pair[0] + 1 )

    print(valid_count)

    