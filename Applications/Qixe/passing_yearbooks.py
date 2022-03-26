
def findSignatureCounts(arr):
    L = len(arr)
    res = [0] * L
    # set of visited students
    visited = set()
    for i in range(len(arr)):
        if i not in visited:
            j = i
            # the students of the same group as student i
            group = set([i])
            # keep passing the yearbook until it goes back to i
            while arr[j]-1 != i:
                j = arr[j]-1
                group.add(j)
            # update the visited set
            visited.update(group)
            for k in group:
                res[k] = len(group)
    return res

# O(n^2) solution (brute-force)
def FindSignatureCountsBF(bookHolders):
    signCounts = [1] * len(bookHolders)
    for student in bookHolders:
        studentIndex = student - 1
        while bookHolders[studentIndex] != student:
            signCounts[studentIndex] += 1
            studentIndex = bookHolders[studentIndex] - 1

    return signCounts

if __name__ == '__main__':
    R = []
    R.append([2,1]) # [2, 2]
    R.append([1,2]) # [1, 1]
    R.append([4,3,2,5,1]) # [3,2,2,3,3]
    for r in R:
        print(r,FindSignatureCountsBF(r))
        

    