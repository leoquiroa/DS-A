def solution(A):
    A.sort()
    ix = 0
    while ix < len(A):
        if len(A[ix:]) == 1: return A[ix]
        f_s = A[ix+1]-A[ix]
        if f_s == 0:
            ix += 2
        else:
            return A[ix]
            
if __name__ == '__main__':
    A = []
    A.append([9, 3, 9, 3, 9, 7, 9])
    A.append([9, 3, 9, 3, 9, 7, 9, 7, 10])
    A.append([9, 3, 9, 3, 9, 7, 9, 7, 1])
    A.append([9, 3, 9, 3, 9, 7, 9, 7, 2])
    A.append([9, 3, 9, 3, 9, 7, 9, 7, 3])
    A.append([9, 3, 9, 3, 9, 7, 9, 7, 4])
    A.append([9, 3, 9, 3, 9, 7, 9, 7, 5])
    for a in A:
        print(a,solution(a))