def solution(X, A):
    # write your code in Python 3.6
    control = {x:0 for x in range(1,X+1)}
    ix = 0
    for a in A:
        if a not in control: continue
        control[a] = 1
        if sum(control.values()) == X: 
            return ix
        ix += 1
    return -1

if __name__ == '__main__':
    A = [3,4,5,6]
    #A = [5]
    new_list = [1, 3, 1, 4, 2, 3, 5, 4]
    for a in A:
        print(a,solution(a,new_list))