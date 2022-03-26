import math

def findMaxProduct(arr):
    result = [-1] * len(arr)
    min_list = arr[:3]
    min_list.sort()
    result[2] = math.prod(min_list)
    ix = 3
    while ix < len(arr):
        min_ele = min_list[0]
        new_ele = arr[ix] if arr[ix] > min_ele else min_ele
        result[ix] = (result[ix-1]/min_ele)*new_ele

        if new_ele > min_list[-1]:
            min_list.append(new_ele)
            min_list = min_list[1:]
        elif new_ele > min_list[1]:
            min_list[0] = min_list[1]
            min_list[1] = new_ele
        else:
            min_list[0] = new_ele
        
        #result[ix] = math.prod(min_list)
        ix += 1
    return result

if __name__ == '__main__':
    R = []
    R.append([2, 4, 7, 1, 5, 3]) # [-1, -1, 56, 56, 140, 140]
    R.append([1, 2, 3, 4, 5]) # [-1, -1, 6, 24, 60]
    R.append([2, 1, 2, 1, 2]) # [-1, -1, 4, 4, 8]
    
    for r in R:
        print(r,findMaxProduct(r))
        

    