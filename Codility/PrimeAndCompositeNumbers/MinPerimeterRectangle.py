import math

def solution(N):
    # write your code in Python 3.6
    squareRootN = math.sqrt(N)
    squareRootN = int(squareRootN) 
    factor = 0
    perimeter = 0
    minPerimeter = 9097290499
    
    if math.pow(squareRootN, 2) != N:
        #round up for any non-perfect squares
        squareRootN += 1
    else:
        #perfect square root won't be reached inside loop 
        # so calculate and set min perimeter
        minPerimeter = int(2 * (squareRootN + squareRootN))

    for i in range(1,squareRootN):
        if N % i == 0:
            #calculate 2nd factor by simple division since know 1st factor and N
            factor = N / i
            perimeter = int(2 * (factor + i))
            minPerimeter = min(perimeter, minPerimeter)

    return minPerimeter


if __name__ == '__main__':
    N = []
    N.append(30)
    N.append(25)
    N.append(10)
    for n in N:
        print(n,solution(n))