
def numberOfWays(arr, desired):
    my_dict = {}
    for item in arr:
        if item not in my_dict:
            my_dict[item] = 1
        else:
            my_dict[item] +=1
    
    counter = 0
    skip_values = []
    for k,v in my_dict.items():
        if k in skip_values: continue
        is_missing = desired-k
        if is_missing in my_dict:
            skip_values.append(is_missing)
            counter += 1 * v
    return counter

def numberOfWays1(arr, k):
    m = [0] * (k+1)
    n = len(arr)
    # Store counts of all elements in map m
    for i in range(0, n):
        m[arr[i]] += 1
 
    twice_count = 0

    # Iterate through each element and increment
    # the count (Notice that every pair is
    # counted twice)
    for i in range(0, n):
 
        missing = k - arr[i]
        twice_count += m[missing]
 
        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is  decreased by one such
        # that the (arr[i], arr[i]) pair is not
        # considered
        if (missing == arr[i]):
            twice_count -= 1
 
    # return the half of twice_count
    return int(twice_count / 2)

if __name__ == '__main__':
    R = []
    R.append([[1, 5, 3, 3, 3],6]) # 4
    R.append([[1, 2, 3, 4, 3],6]) # 2
    for r in R:
        print(numberOfWays1(r[0],r[1]),r)
        

    