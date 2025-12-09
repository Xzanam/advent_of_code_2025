import sys


def isValidRowCol(row , col, rows, cols) -> bool : 
    if(row >= 0  and row <  rows) and  (col >= 0 and col < cols) : 
        return True 
    return False


def count_paperrolls(grid: list) -> int:
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    total_rolls = 0

    for r in range(rows):
        for c in range(cols):

            print(f"Checking cell ({r}, {c}): {grid[r][c]}")

            if(grid[r][c] == '.'): 
                continue

            neighbours_count = 0

            if(isValidRowCol(r, c + 1, rows, cols)) :
                if( grid[r][c + 1] == '@'):
                    neighbours_count += 1
                    print(f"Right neighbour at ({r}, {c + 1}) is '@'")
            
            if(isValidRowCol(r, c - 1, rows, cols)) :
                if(grid[r][c - 1] == '@'):
                    neighbours_count += 1
                    print(f"Left neighbour at ({r}, {c - 1}) is '@'")

            if(isValidRowCol(r + 1, c , rows, cols)) :
                if(grid[r + 1][c] == '@'):
                    neighbours_count += 1
                    print(f"Bottom neighbour at ({r + 1}, {c}) is '@'")


            if(isValidRowCol(r - 1, c , rows, cols)) :
                if(grid[r - 1][c] == '@'):
                    neighbours_count += 1
                    print(f"Top neighbour at ({r - 1}, {c}) is '@'")

            if(isValidRowCol(r + 1, c  + 1, rows, cols)) :
                if(grid[r + 1][c+1] == '@'):
                    neighbours_count += 1
                    print(f"Bottom-right neighbour at ({r + 1}, {c + 1}) is '@'")


            if(isValidRowCol(r + 1, c - 1 , rows, cols)) :
                if(grid[r + 1][c-1] == '@'):
                    neighbours_count += 1
                    print(f"Bottom-left neighbour at ({r + 1}, {c - 1}) is '@'")


            if(isValidRowCol(r - 1, c+1 , rows, cols)) :
                if(grid[r - 1][c+1] == '@'):
                    neighbours_count += 1
                    print(f"Top-right neighbour at ({r - 1}, {c + 1}) is '@'")


            if(isValidRowCol(r - 1, c -1  , rows, cols)) :
                if(grid[r - 1][c-1] == '@'):
                    neighbours_count += 1
                    print(f"Top-left neighbour at ({r - 1}, {c - 1}) is '@'")

            print(f"total neighbours for {r}{c} : {neighbours_count}")
            if(neighbours_count < 4 ) : 
                total_rolls += 1
            


    return total_rolls

if __name__ == "__main__" :

    grid = []

    for line in sys.stdin : 
        line = line.rstrip("\n")
        if not line:
            continue
        grid.append(line)

    print(count_paperrolls(grid) )
