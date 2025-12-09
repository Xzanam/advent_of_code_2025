import bisect

# Ranges input as list of tuples
ranges = [(3,5),(10,14),(16,20),(12,18)]
ids = [1,5,8,11,17,32]

# 1. Sort
ranges.sort()

# 2. Merge
merged = []

for start, end in ranges:
    if not merged or start > merged[-1][1] + 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

# Extract starts separately for bisect
starts = [a for a, b in merged]

# 3. Count fresh
count = 0
for x in ids:
    i = bisect.bisect_right(starts, x) - 1
    if i >= 0 and merged[i][0] <= x <= merged[i][1]:
        count += 1

print(count)
