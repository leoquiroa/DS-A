def solution(A,B,m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    for i in range(n):
        for j in range(n):
            change = B[j] - A[i]
            sum_a += change
            sum_b -= change
            if sum_a == sum_b:
                return True
            sum_a -= change
            sum_b += change
    return False

if __name__ == '__main__':
    A = [5, 3, 1, 4, 2]
    #B = [1, 2, 3, 4, 5] 
    B = [3, 5, 1, 4, 2] 
    solution(A,B,3)