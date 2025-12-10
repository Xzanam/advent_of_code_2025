
import sys
from collections import Counter

def get_timeline_count(grid : list) -> int: 
    size_x = len(grid[0])
    size_y = len(grid)

    track_beams = Counter()
    track_beams[size_x // 2 ]  += 1;

    for i in range(1, size_y):
        for x in track_beams.copy(): 
            if grid[i][x] == "^" : 
                track_beams[x + 1] += track_beams[x]
                track_beams[x - 1] += track_beams[x]
                track_beams.pop(x)
        # y = [track_beams[j] if track_beams[j] else 0 for j in range(size_x)]
        # print(track_beams)
        # print(y)
        

    
    # print(track_beams)
    return (sum(track_beams.values()))




if __name__ == "__main__":

    grid  = []
    for line in sys.stdin:
        if not line:
            continue
        grid.append(line.strip())

    print(get_timeline_count(grid))



