
def balancedSplitExists(arr):
    arr.sort()
    m = len(arr)//2
    total_sum = sum(arr)

    left = sum(arr[:m])
    right = total_sum - left
    if left == right: 
        return not any(x in arr[m+1:] for x in arr[:m+1])

    while True:
        left += arr[m]
        right -= arr[m]
        if left == right: 
            return not any(x in arr[m+1:] for x in arr[:m+1])
        m += 1
        if m >= len(arr)-1: return False

if __name__ == '__main__':
    R = []
    R.append([12, 7, 6, 1, 2]) # False
    R.append([2, 1, 2, 5]) # True
    R.append([3, 6, 3, 4, 4]) # False
    R.append([1, 5, 7, 1]) # True
    R.append([12, 7, 6, 7, 6]) # False
    
    for r in R:
        print(r,balancedSplitExists(r))
        

    