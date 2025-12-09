
def recursive_find(largest_num : list, input_string:str,  idx: int) -> int  : 
    size_num = len(largest_num)
    if(size_num == 12) : 
        return

    size = len(input_string)
    curr_largest = 0
    curr_idx = 0

    for i in range(idx + 1, size): 
        if(int(input_string[i]) > curr_largest and  size - i >= 12 - size_num  ) :
            curr_largest = int(input_string[i])
            curr_idx = i

    largest_num.append(curr_largest)
    return recursive_find(largest_num, input_string, curr_idx )



if __name__ == "__main__" :
    import sys

    myList = []
    total = 0
    for line in sys.stdin :
        line = line.rstrip("\n")
        if not line:
            continue
        recursive_find(myList,line, -1 );
        # total = int(''.strip(","))
        total  += int(''.join([str(i) for i in myList]))
        myList.clear()

    print(total)
    

    









