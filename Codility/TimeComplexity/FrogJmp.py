import math

def solutionA(X,Y,D):
    # write your code in Python 3.6
    counter = 0 
    while X < Y:
        counter += 1
        X += D
    return counter

def solutionB(X,Y,D):
    # write your code in Python 3.6
    return math.ceil((Y-X)/D)

if __name__ == '__main__':
    A = []
    A.append([10,85,30])
    A.append([10,15,30])
    A.append([10,40,30])
    for a in A:
        print(a,solutionB(a[0],a[1],a[2]))