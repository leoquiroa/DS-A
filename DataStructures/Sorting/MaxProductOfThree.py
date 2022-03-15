from functools import reduce

def solutionA(A):
    pos = [x for x in A if x>0]
    neg = [x for x in A if x<0]
    if len(pos)<3 and len(neg)%2 == 0:
        neg = [abs(x) for x in neg]
        pos += neg 
        pos.sort()
        values = pos[-3:]
    else:
        A.sort()
        values = A[-3:]
    return reduce((lambda x, y: x * y), values)

def solutionB(A):
    A.sort()
    N = len(A)
    op1 = A[N-1]*A[0]*A[1]
    op2 = A[N-1]*A[N-2]*A[N-3]
    return max(op1,op2)

if __name__ == '__main__':
    A = []
    A.append([-3, 1, 2, -2, 5, 6])
    A.append([-5, 5, -5, 4])
    A.append([-4, -6, 3, 4, 5])
    for a in A:
        print(a,solutionB(a))