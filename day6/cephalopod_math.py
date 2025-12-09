
import sys
import numpy as np

def calc_sum(nums : np.array, operators : list) -> int:
    result = []
    for i in range(len(operators)) :
        if operators[i] == "+" : 
            result.append(sum(nums[i]));
        elif operators[i] == "*" :
            result.append(np.prod(nums[i]));
    return sum(result)


if __name__ == "__main__" : 

    nums = []
    operators  = []
    for line in sys.stdin:
        if not line: 
            continue
        try: 
            nums.append(list( map( int, line.split() ) ))
        except ValueError : 
            operators = line.split()
        
    nums = np.array(nums).transpose()

    print( calc_sum(nums, operators) )






        



