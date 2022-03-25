import math

def solution(N):
    # write your code in Python 3.6
    squareRootN = math.sqrt(N)
    squareRootN = int(squareRootN)
    factors = 0
    if math.pow(squareRootN, 2) != N:
        #round up for any non-perfect squares
        squareRootN += 1
    else:
        #perfect squares have an additional factor
        factors += 1

    for i in range(1,squareRootN):
        if N % i == 0:
            factors += 2

    return factors
        


if __name__ == '__main__':
    N = []
    N.append(24)
    N.append(25)
    N.append(10)
    for n in N:
        print(n,solution(n))