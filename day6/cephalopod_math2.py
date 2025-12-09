
import sys
import numpy as np

def get_nums(nums : list) -> list:
    size_x = len(nums[0])
    size_y = len(nums)
    result = []
    print(nums[0][14])
    inter_list = []
    x = 0
    for i in range(size_x) : 
        curr = nums[0][x] +  nums[1][x] + nums[2][x]  + nums[3][x]
        print(f"curr: {curr} , x: {x}")
        if( curr.strip()) :
            inter_list.append(int(curr.strip()))
        else:
            result.append(inter_list.copy())
            inter_list.clear()
        x += 1
    return result















if __name__ == "__main__":
    nums = []
    operators  = []
    for line in sys.stdin:
        if not line: 
            continue
        nums.append(line)
    operators = list(nums.pop().split())
    result = get_nums(nums)
    final_result = []


    for i in range(len(operators)) : 
        match(operators[i]) :
            case "+" :
                final_result.append(np.sum(result[i]))
            case "*" :
                final_result.append(np.prod(result[i]))

    print( sum(final_result) )

 
