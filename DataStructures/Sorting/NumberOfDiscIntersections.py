def solutionA(A):
    # write your code in Python 3.6
    
    lower,upper = [],[]
    for i,a in enumerate(A):
        lower.append(i - a)
        upper.append(i + a)
    
    lower.sort()
    upper.sort()

    intersections = 0
    j = 0
    i = 0
    while i < len(A):
        while j < len(A) and upper[i] >= lower[j]:
            intersections += j
            intersections -= i
            j += 1
        i += 1

    if intersections > 10000000: return -1
    return intersections

def solutionB(A):
    # write your code in Python 3.6
    
    lower,upper = [],[]
    for i,a in enumerate(A):
        lower.append(i - a)
        upper.append(i + a)
    
    lower.sort()
    upper.sort()

    intersections = 0
    i = 0
    while i < len(A):
        j = i+1
        while j < len(A):
            if upper[i] >= lower[j]:
                intersections += 1
            j += 1
        i += 1

    if intersections > 10000000: return -1
    return intersections

def solutionC(A):
    # write your code in Python 3.6
    
    lower,upper = [],[]
    for i,a in enumerate(A):
        lower.append(i - a)
        upper.append(i + a)
    
    #lower.sort()
    #upper.sort()

    intersections = 0
    i = 0
    while i < len(A):
        j = i+1
        while j < len(A):
            if upper[i] >= lower[j]:
                intersections += 1
            j += 1
        i += 1

    if intersections > 10000000: return -1
    return intersections

if __name__ == '__main__':
    A = []
    A.append([1, 5, 2, 1, 4, 0])
    for a in A:
        print(a,solutionC(a))