
import sys



def  get_tachyon_count(grid: list) -> int:
    size_x = len(grid[0])
    size_y = len(grid)

    track_beams = {size_x // 2}
    tachyon_count = 0
    for i in range(1,size_y) : 
        for x in track_beams.copy():
            if grid[i][x] == "^":
                tachyon_count += 1
                track_beams.add(x - 1)
                track_beams.add(x + 1)
                track_beams.remove(x)

    return tachyon_count









if __name__ == "__main__":

    grid  = []
    for line in sys.stdin:
        if not line:
            continue
        grid.append(line.strip())

    result = get_tachyon_count(grid)
    print(result)
