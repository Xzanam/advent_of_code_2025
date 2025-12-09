import sys


def isValidRowCol(row , col, rows, cols) -> bool : 
    if(row >= 0  and row <  rows) and  (col >= 0 and col < cols) : 
        return True 
    return False


def remove_at_idx(grid: list, idxes: list ) :
    for r, c in idxes :
        grid[r][c] = "."

# def rec_count_paperrolls(grid: list ,  total : int  )  :
#     par_total, idxes = count_paperrolls(grid)
#     if(par_total == 0): 
#         return total

#     remove_at_idx(grid, idxes)
#     total += par_total
#     rec_count_paperrolls(grid, total)

def rec_count_paperrolls(grid: list, total: int) -> int:

    par_total, idxes = count_paperrolls(grid)

    if par_total == 0:
        return total
    
    remove_at_idx(grid, idxes)
    total += par_total
    return rec_count_paperrolls(grid, total)


def count_paperrolls(grid: list) -> tuple[int, list] :
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    total_rolls = 0
    idx_to_remove = []

    for r in range(rows):
        for c in range(cols):
            print(f"Checking cell ({r}, {c}): {grid[r][c]}")

            if(grid[r][c] == '.'): 
                continue

            neighbours_count = 0

            if(isValidRowCol(r, c + 1, rows, cols)) :
                if( grid[r][c + 1] == '@'):
                    neighbours_count += 1
            
            if(isValidRowCol(r, c - 1, rows, cols)) :
                if(grid[r][c - 1] == '@'):
                    neighbours_count += 1

            if(isValidRowCol(r + 1, c , rows, cols)) :
                if(grid[r + 1][c] == '@'):
                    neighbours_count += 1


            if(isValidRowCol(r - 1, c , rows, cols)) :
                if(grid[r - 1][c] == '@'):
                    neighbours_count += 1

            if(isValidRowCol(r + 1, c  + 1, rows, cols)) :
                if(grid[r + 1][c+1] == '@'):
                    neighbours_count += 1


            if(isValidRowCol(r + 1, c - 1 , rows, cols)) :
                if(grid[r + 1][c-1] == '@'):
                    neighbours_count += 1


            if(isValidRowCol(r - 1, c+1 , rows, cols)) :
                if(grid[r - 1][c+1] == '@'):
                    neighbours_count += 1


            if(isValidRowCol(r - 1, c -1  , rows, cols)) :
                if(grid[r - 1][c-1] == '@'):
                    neighbours_count += 1

            print(f"total neighbours for {r}{c} : {neighbours_count}")
            if(neighbours_count < 4 ) : 
                total_rolls += 1
                idx_to_remove.append( (r,c) )
                
            


    return (total_rolls , idx_to_remove)

if __name__ == "__main__" :

    grid = []

    for line in sys.stdin : 
        line = line.rstrip("\n")
        if not line:
            continue
        grid.append(list(line))
    
    total = 0
    print(rec_count_paperrolls(grid, total))

    print(total)


