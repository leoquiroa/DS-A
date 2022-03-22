def solution(A):
    # write your code in Python 3.6
    profit = 0
    for ix,a in enumerate(A):
        for b in A[ix+1:]:
            calc = b-a
            if calc > profit:
                profit = calc
                print(a,b,profit)
    return 0 if profit <= 0 else profit

def solutionB(A):
    # write your code in Python 3.6
    if len(A) == 0 : return 0
    min_val = min(A)
    min_ix = A.index(min_val)
    profit = 0
    for a in A[min_ix:]:
        calc = a-min_val
        if calc > profit:
            profit = calc
            print(a,profit)
    return 0 if profit <= 0 else profit

def solutionC(A):
    # write your code in Python 3.6
    if len(A) < 2 : return 0
    delta = [a-A[ix] for ix,a in enumerate(A[1:])]
    
    absolute_max = delta[0]
    local_max = delta[0]
    next_sum = 0

    for ix,_ in enumerate(delta):
        if ix == 0: continue
        next_sum = local_max + delta[ix]
        local_max = max(delta[ix], next_sum)
        absolute_max = max(absolute_max, local_max)

    if absolute_max > 0: return absolute_max
    return 0



if __name__ == '__main__':
    A = []
    A.append([23171,21011,21123,21366,21013,21367])
    A.append([8, 9, 3, 6, 1, 2])
    for a in A:
        print(a,solutionC(a))