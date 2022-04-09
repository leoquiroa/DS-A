

def solutionA(M, A):
    visited = [False]*(M+1)
    front = 0
    N = len(A)
    total = 0
     
    for back in range(N):
        
        while(front < N and visited[A[front]] == False):
            visited[A[front]] = True
            front += 1
        
        total += front - back
        visited[A[back]] = False
        
        if(total > 1000000000):
            return 1000000000
            
    return total  

def solutionB(M, A):
    sum = 0
    front = 0
    back = 0
    my_set = set()
    while front < len(A):
        while front < len(A) and A[front] not in my_set:
            sum += (front-back+1)
            my_set.add(A[front])
            front += 1
        while A[back] != A[front]:
            my_set.remove(A[back])
            back += 1
        my_set.remove(A[back])
        back += 1        
    return min(sum, 1000000000)
    
def solutionC(M, A):
    seen = [False]*(M+1)
    leftEnd = 0
    rightEnd = 0
    numSlice = 0
    # key point: move the "leftEnd" and "rightEnd" of a slice
    while leftEnd < len(A) and rightEnd < len(A):
        # case 1: distinct (rightEnd)
        if seen[A[rightEnd]] == False:
            # note: not just +1 
            # there could be (rightEnd - leftEnd + 1) combinations (be careful)
            numSlice = numSlice + (rightEnd - leftEnd + 1)
            if numSlice >= 1000000000: return 1000000000
            
            # increase the slice to right by "1" (important)
            seen[A[rightEnd]] = True
            rightEnd += 1
        # case 2: not distinct
        else: 
            # decrease the slice from left by "1" (important)
            # remove A[leftEnd] from "seen" (be careful)
            seen[A[leftEnd]] = False
            leftEnd += 1 
    
    return numSlice

 
if __name__ == '__main__':
    R = []
    R.append([6,[3,4,5,5,2]]) #9
    R.append([6,[3,4,5,6,2,2]]) #16
    for r in R:
        print(r,solutionC(r[0],r[1]))