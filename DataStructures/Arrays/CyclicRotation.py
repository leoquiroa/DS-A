def solution(A, K):
    if len(A) == 0: return []
    while K > 0:
        A = [A[-1]] + A[:-1]
        K -= 1
    return A

if __name__ == '__main__':
    A = [3, 8, 9, 7, 6]
    K = 3
    solution(A, K)