
def are_they_equal(array_a, array_b):

    # Integer variable for
    # storing the required
    # starting and ending
    # indices in the array

    N = len(array_a)
    start = 0
    end = N - 1

    # Finding the smallest index
    # for which A[i] != B[i]
    # i.e the starting index
    # of the unequal sub-array

    for i in range(N):
        if array_a[i] != array_b[i]:
            start = i
            break

    # Finding the largest index
    # for which A[i] != B[i]
    # i.e the ending index
    # of the unequal sub-array

    for i in range(N - 1, -1, -1):
        if array_a[i] != array_b[i]:
            end = i
            break

    # Reversing the sub-array
    # A[start], A[start+1] .. A[end]

    array_a[start:end + 1] = reversed(array_a[start:end + 1])

    # Checking whether on reversing
    # the sub-array A[start]...A[end]
    # makes the arrays equal

    for i in range(N):
        if array_a[i] != array_b[i]:

            # If any element of the
            # two arrays is unequal
            # print No and return

            return False

    # Print Yes if arrays are
    # equal after reversing
    # the sub-array

    return True


if __name__ == '__main__':
    R = []
    R.append([[1, 2, 3, 4],[1, 4, 3, 2]]) # True
    R.append([[1, 2, 3, 4],[1, 2, 3, 5]]) # False
    for r in R:
        print(are_they_equal(r[0],r[1]),r)
        

    