def solution(A):
    # write your code in Python 3.6
    counter = 0
    for ix,a in enumerate(A):
        if a == 0:
            counter += len([x for x in A[ix+1:] if x == 1])
    return counter


if __name__ == '__main__':
    A = []
    A.append([0, 1, 0, 1, 1])
    for a in A:
        print(a,solution(a))