
from numpy import array_split


def countDistinctTriangles(arr):
    control = []
    for element in arr:
        unique = set(element)
        if unique not in control:
            control.append(unique)
    return len(control)


if __name__ == '__main__':
    R = []
    R.append([(7, 6, 5), (5, 7, 6), (8, 2, 9), (2, 3, 4), (2, 4, 3)]) # 3
    R.append([(3, 4, 5), (8, 8, 9), (7, 7, 7)]) # 3
    R.append([[2, 2, 3], [3, 2, 2], [2, 5, 6]]) # 2
    R.append([[8, 4, 6], [100, 101, 102], [84, 93, 173]]) # 3
    R.append([[5, 8, 9], [5, 9, 8], [9, 5, 8], [9, 8, 5], [8, 9, 5], [8, 5, 9]]) # 1
    for r in R:
        print(r,countDistinctTriangles(r))
        

    