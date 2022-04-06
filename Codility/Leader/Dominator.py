from re import X


def solution(A):
    # write your code in Python 3.6
    #A.sort()
    control = {}
    max_ix = -1
    for a in A:
        if a in control:
            control[a] += 1
            if control[a] > len(A)/2: 
                max_ix = a
                break
        else:
            control[a] = 1
    if max_ix == -1: return -1
    return A.index(max_ix)

if __name__ == '__main__':
    A = []
    A.append([3, 4, 3, 2, 3, -1, 3, 3])
    A.append([2, 1, 4, 7, 4, 8, 3, 6, 4, 7])
    for a in A:
        print(a,solution(a))


