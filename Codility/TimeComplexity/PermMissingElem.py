def solution(A):
    # write your code in Python 3.6
    if len(A) == 0: return 1
    cond1 = [x for x in range(1,len(A)+1+1)]
    res = set(cond1) - set(A)
    if len(res) == 0: return 1
    return int(list(res)[0])

if __name__ == '__main__':
    A = []
    A.append([2,3,1,5])
    A.append([2,3,4,5])
    A.append([1])
    A.append([1,2])
    for a in A:
        print(a,solution(a))