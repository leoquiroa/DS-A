def solution(A):
    # write your code in Python 3.6
    cond1 = [x for x in range(1,len(A)+1)]
    return 1 if set(cond1) == set(A) else 0

if __name__ == '__main__':
    A = []
    A.append([4,1,3,2])
    A.append([4,1,3])
    for a in A:
        print(a,solution(a))