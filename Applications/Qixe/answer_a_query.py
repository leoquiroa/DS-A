import math

def answer(arr):
    control = [False] * len(arr)
    result = []
    for a in arr:
        if a[0] == 1: # SET
            control[a[1]-1] = True
        elif a[0] == 2: # GET
            sub = control[a[1]-1:]
            index = sub.index(True)+1 if True in sub else -1
            result.append(index)

if __name__ == '__main__':
    R = []
    R.append([[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]]) # [-1, 2, -1, 2]
    for r in R:
        print(r,answer(r))
        

    