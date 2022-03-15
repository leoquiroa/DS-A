def solution(A):
    A.sort()
    ix = 0
    limit = len(A)-2
    while ix < limit:
        #print(A[ix:ix+3])
        P = A[ix]
        Q = A[ix+1]
        R = A[ix+2]
        if (P+Q)>R and (Q+R)>P and (R+P)>Q: return 1 
        ix += 1
    return 0

if __name__ == '__main__':
    A = []
    A.append([10, 2, 5, 1, 8, 20])
    A.append([10, 50, 5, 1])
    for a in A:
        print(a,solution(a))