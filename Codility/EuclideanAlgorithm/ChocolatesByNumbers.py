import math

def solution(N,M):
    my_dict = {x:0 for x in range(0,N)}
    ix = 0
    my_dict[ix] = 1
    ctrl_ix = 1
    while True:
        ix = (ix + M) % N
        if my_dict[ix] == 0:
            my_dict[ix] = 1
            ctrl_ix += 1
        else: break
    return ctrl_ix

def solutionA(N,M):
    control = 0
    divisor = M
    dividendo = N
    cociente = dividendo//divisor
    resto = (dividendo/divisor - cociente)
    if resto == 0: return cociente
    control = cociente
    while resto > 0:
        new_start = M - round(resto * M,0)
        cociente = (N-new_start)//M
        resto = (N-new_start)/M - cociente
        control += cociente + 1
    return control

def solutionB(N,M):
    return N/gcdByDivision(N, M)

def gcdByDivision(A, B):
    if A % B == 0: 
        return B
    else: 
        return gcdByDivision(B, A % B)
 


    
if __name__ == '__main__':
    R = []
    R.append([10,2])
    R.append([10,3])
    R.append([10,4])
    R.append([10,5])
    R.append([10,6])
    for r in R:
        print(r,solutionB(r[0],r[1]))