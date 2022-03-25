
def count_subarrays1(arr):
    response = []
    for ix,element in enumerate(arr):
        if element == 1: 
            response.append(element)
        else:
            counter = 1
            right = arr[ix:]
            left = arr[:ix]

            
            iix = len(left)-1
            while iix >= 0:
                if left[iix] < element:
                    counter +=1
                else:
                    break
                iix -= 1

            for l in right[1:]:
                if l < element:
                    counter +=1
                else:
                    break
            
            response.append(counter)
    return response

def count_subarrays2(arr):
    n = len(arr)
    res = [1] * n
    stack = [-1]
    #left
    for i in range(n):
        while len(stack) > 1 and arr[stack[-1]] < arr[i]:
            stack.pop()
        res[i] += i - stack[-1] - 1
        stack.append(i)
    #right
    stack = [n]
    for i in range(n - 1, -1, -1):
        while len(stack) > 1 and arr[stack[-1]] < arr[i]:
            stack.pop()
        res[i] += stack[-1] - i - 1
        stack.append(i)
    return res

if __name__ == '__main__':
    R = []
    R.append([3, 4, 1, 6, 2]) #[1, 3, 1, 5, 1]
    R.append([2, 4, 7, 1, 5, 3]) #[1, 2, 6, 1, 3, 1]
    for r in R:
        print(count_subarrays2(r))
        

    