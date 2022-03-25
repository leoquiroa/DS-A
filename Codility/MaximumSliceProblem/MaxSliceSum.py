def solution(A):
    # write your code in Python 3.6
    previous  = A[0]
    current  = A[0]
    _global = A[0]

    for ix,a in enumerate(A):
        if ix == 0: continue
        current = max(A[ix], previous + A[ix])
        previous = current
        _global = max(_global, current)
        print(a,current,previous,_global)
    return _global

def solutionB(A):
    # write your code in Python 3.6
    max_so_far = 0
    max_ending_here = 0

    for a in A:
        max_ending_here = max_ending_here + a
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here 
        if max_ending_here < 0:
            max_ending_here = 0     
    return max_so_far


def solutionC(A):
    # write your code in Python 3.6
    max_so_far = 0
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
 
    for i in range(0,len(A)):
 
        max_ending_here += a[i]
 
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
 
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
    
    print(start,end,max_so_far)



if __name__ == '__main__':
    A = []
    A.append([-2, -3, 4, -1, -2, 1, 5, -3])
    A.append([3,2,-6,4,0])
    A.append([10])
    A.append([-2, 1])
    for a in A:
        print(a,solution(a))