import sys



def count_fresh_ingredients(ranges, ingredients):
    fresh_count = 0

    for ingredient in ingredients:
        is_fresh = False
        for r in ranges:
            if r[0] <= ingredient <= r[1]:
                is_fresh = True
                break

        if is_fresh:
            fresh_count += 1

    return fresh_count




if __name__ == "__main__" :

    flag = False
    ranges = []
    ingredients = []
    for line in sys.stdin : 
        line = line.rstrip("\n")
        if not line:
            flag = True
            continue
        if not flag:
            ranges.append( tuple( map(int, line.split('-'))))
        else: 
            ingredients.append(int(line))
        
    result = count_fresh_ingredients(ranges, ingredients)
    print(result)





