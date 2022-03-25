from functools import reduce

def solutionA(A):
    # write your code in Python 3.6
    ix = 1
    diffs = []
    while ix < len(A):
        left = reduce((lambda x, y: x + y), A[:ix])
        right = reduce((lambda x, y: x + y), A[ix:])
        ix += 1
        diffs.append(abs(left-right))
        print(left,right)
    return min(diffs)

def solutionB(A):
    # write your code in Python 3.6
    ix = 1
    the_min = 0
    first = True
    sum_all = sum(A)
    while ix < len(A):
        left = sum(A[:ix])
        right = sum_all - left
        ix += 1
        diff = abs(left-right)
        if first == True: 
            first = False
            the_min = diff
        the_min = min(the_min,diff)
        #if diff == 1: return diff
        #print(left,right)
    return the_min

def solutionC(A):
    left = A[0]
    right = sum(A[1:])
    diff = abs(left - right)

    for p in range(1, len(A)):
        ldiff = abs(left - right)
        if ldiff < diff:
            diff = ldiff
        left += A[p]
        right -= A[p]
    
    return diff

if __name__ == '__main__':
    A = []
    A.append([3, 1, 2, 4, 3])
    A.append([1, 2, 3, 4, 2])
    for a in A:
        print(a,solutionC(a))