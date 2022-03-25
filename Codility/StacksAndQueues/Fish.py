
def solution(A,B):
    # write your code in Python 3.6
    if len(A) == 0: return 0
    fish_alive = len(A)
    ix = 0
    stack = []
    while ix < len(A):
        if B[ix] == 1: #downstream
            stack.append(A[ix])
        elif B[ix] == 0: #upstream
            while len(stack) > 0:
                if stack[-1] > A[ix]:
                    fish_alive -= 1
                    break
                elif stack[-1] < A[ix]:
                    fish_alive -= 1
                    stack.pop()
        ix += 1
    return fish_alive
        

    

if __name__ == '__main__':
    A = []
    A.append([[4, 3, 2, 1, 5], [0, 1, 0, 0, 0]])
    A.append([[4, 3, 2, 1, 5], [0, 0, 0, 0, 0]])
    A.append([[4, 3, 2, 1, 5], [1, 0, 0, 0, 0]])
    for a in A:
        print(a,solution(a[0],a[1]))